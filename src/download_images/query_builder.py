"""
Search query generation for Wikimedia Commons.
Single Responsibility: Build intelligent search queries from character data.
Open/Closed Principle: Easy to extend with new query strategies.
"""
from typing import List
from .text_parser import YearExtractor, NameParser, BiographyParser
from .config import DownloadConfig


class QueryStrategy:
    """Base class for query generation strategies."""

    def generate(self, name: str, actual_name: str, context: dict) -> List[str]:
        """
        Generate queries based on this strategy.

        Args:
            name: Original character name
            actual_name: Parsed/normalized name
            context: Dictionary with keys: years, country, title, dynasty, char_type

        Returns:
            List of query strings
        """
        raise NotImplementedError


class BuildingQueryStrategy(QueryStrategy):
    """Query strategy for buildings and places (type T, B)."""

    def generate(self, name: str, actual_name: str, context: dict) -> List[str]:
        """Generate queries for buildings/architecture."""
        return [
            f"{name} architecture",
            f"{name} photograph",
            f"{name} building",
            f"{name} cityscape",
        ]


class PersonQueryStrategy(QueryStrategy):
    """Query strategy for historical persons."""

    def generate(self, name: str, actual_name: str, context: dict) -> List[str]:
        """Generate queries for persons based on available context."""
        queries = []
        years = context.get('years', [])
        country = context.get('country')
        title = context.get('title')
        dynasty = context.get('dynasty')

        # Strategy 1: Most specific - actual name + country + title
        if country and title:
            queries.append(f"{actual_name} {country} {title} portrait")
            queries.append(f"{actual_name} {country} portrait")

        # Strategy 2: Actual name + country (very important for disambiguation)
        if country:
            queries.append(f"{actual_name} {country} portrait")
            # Only use bare surname if it's not ambiguous (avoid single-word names)
            if ' ' in actual_name or len(name) > 10:  # Multi-word or long name
                queries.append(f"{name} {country} portrait")

        # Strategy 3: Actual name + title
        if title:
            queries.append(f"{actual_name} {title} portrait")

        # Strategy 4: Actual name + dynasty
        if dynasty:
            queries.append(f"{actual_name} {dynasty} portrait")

        # Strategy 5: Actual name + year (for disambiguation)
        if years:
            queries.append(f"{actual_name} {years[0]} portrait")
            # Include country with year for better results
            if country:
                queries.append(f"{actual_name} {country} {years[0]} portrait")

        # Strategy 6: Actual name only
        queries.append(f"{actual_name} portrait")
        queries.append(f"{actual_name} painting")

        # Strategy 7: Original name (fallback)
        if actual_name != name:
            queries.append(f"{name} portrait")

        return queries


class QueryBuilder:
    """
    Builds intelligent search queries using character data.
    Dependency Inversion: Depends on abstractions (QueryStrategy).
    """

    def __init__(self):
        """Initialize query builder with strategies."""
        self.building_strategy = BuildingQueryStrategy()
        self.person_strategy = PersonQueryStrategy()

    def build_queries(self, character) -> List[str]:
        """
        Build intelligent search queries using all available character data.

        Args:
            character: Character object with name, first_names, biography, etc.

        Returns:
            List of search query strings, prioritized by specificity
        """
        # Extract basic information
        name = (character.name or "").strip()
        first_names = (character.first_names or "").strip()
        biography = (character.biography or "").strip()
        birth_date = (character.birth_date or "").strip()
        death_date = (character.death_date or "").strip()
        char_type = (character.type or "").strip()

        if not name:
            return []

        # Select strategy based on character type
        if char_type in ['T', 'B']:
            strategy = self.building_strategy
            actual_name = name
            context = {'char_type': char_type}
        else:
            strategy = self.person_strategy

            # Parse name
            actual_name = name
            if first_names:
                actual_name = NameParser.extract_actual_name(name, first_names)

            # Extract context
            years = []
            years.extend(YearExtractor.extract_years(birth_date))
            years.extend(YearExtractor.extract_years(death_date))
            years.extend(YearExtractor.extract_years(biography))
            years = sorted(set(years))

            country, title, dynasty = BiographyParser.extract_context(biography)

            context = {
                'years': years,
                'country': country,
                'title': title,
                'dynasty': dynasty,
                'char_type': char_type,
            }

        # Generate queries using strategy
        queries = strategy.generate(name, actual_name, context)

        # Remove duplicates while preserving order
        seen = set()
        unique_queries = []
        for q in queries:
            q_normalized = ' '.join(q.lower().split())  # Normalize whitespace
            if q_normalized not in seen:
                seen.add(q_normalized)
                unique_queries.append(q)

        return unique_queries[:DownloadConfig.MAX_QUERIES_PER_CHARACTER]
