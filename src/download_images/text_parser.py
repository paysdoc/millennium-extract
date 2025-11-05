"""
Text parsing utilities for character information.
Single Responsibility: Extract and parse text data from character fields.
"""
import re
from typing import List, Optional, Tuple


class YearExtractor:
    """Extract year information from text."""

    @staticmethod
    def extract_years(text: Optional[str]) -> List[str]:
        """
        Extract 4-digit years from text.

        Args:
            text: Text to extract years from

        Returns:
            List of year strings found in the text
        """
        if not text:
            return []
        # Find all 4-digit numbers that look like years (1000-2029)
        years = re.findall(r'\b(1[0-9]{3}|20[0-2][0-9])\b', text)
        return years


class NameParser:
    """Parse and normalize character names."""

    @staticmethod
    def extract_actual_name(name: str, first_names: str) -> str:
        """
        Extract the actual searchable name by combining name and first_names intelligently.

        Examples:
            name="BARBAROSSA", first_names="Frederick I(Hohenstaufen)"
                -> "Frederick I Barbarossa"
            name="CATHERINE II", first_names="(the Great)"
                -> "Catherine II the Great"
            name="CHARLES II", first_names="(Merry Monarch)"
                -> "Charles II"

        Args:
            name: The primary name (usually surname or title)
            first_names: Additional name information (may contain titles)

        Returns:
            Normalized, searchable name
        """
        # Clean up first_names - remove parentheses and special formatting
        clean_first = first_names.strip('()').strip()

        # If first_names looks like a title/descriptor (like "the Great"), combine with name
        if clean_first.lower().startswith('the '):
            return f"{name} {clean_first}"

        # If first_names contains actual name parts (letters before parentheses)
        # Extract the part before any parentheses
        match = re.match(r'^([^(]+)', clean_first)
        if match:
            actual_first = match.group(1).strip()
            # If it looks like a real name (contains letters and spaces), use it
            if actual_first and not actual_first.lower() in ['king', 'queen', 'emperor', 'empress']:
                return f"{actual_first} {name}"

        # Fallback: just use the name
        return name


class BiographyParser:
    """Parse biography text to extract contextual information."""

    # Country/region mapping for context
    COUNTRY_MAP = {
        'france': 'France',
        'england': 'England',
        'spain': 'Spain',
        'russia': 'Russia',
        'russian': 'Russia',
        'germany': 'Germany',
        'german': 'Germany',
        'italy': 'Italy',
        'italian': 'Italy',
        'austria': 'Austria',
        'prussia': 'Prussia',
        'scotland': 'Scotland',
        'holy roman': 'Holy Roman Emperor',
        'byzantine': 'Byzantine',
        'ottoman': 'Ottoman',
    }

    # Known dynasties
    DYNASTIES = [
        'Stuart', 'Tudor', 'Valois', 'Habsburg', 'Bourbon',
        'Plantagenet', 'Capetian', 'Romanov', 'Hohenstaufen'
    ]

    @staticmethod
    def extract_country(biography: str) -> Optional[str]:
        """
        Extract country/region from biography text.

        Args:
            biography: Biography text

        Returns:
            Country name if found, None otherwise
        """
        if not biography:
            return None

        bio_lower = biography.lower()
        for key, value in BiographyParser.COUNTRY_MAP.items():
            if key in bio_lower:
                return value
        return None

    @staticmethod
    def extract_royal_title(biography: str) -> Optional[str]:
        """
        Extract royal title from biography text.

        Args:
            biography: Biography text

        Returns:
            Royal title if found, None otherwise
        """
        if not biography:
            return None

        bio_lower = biography.lower()

        if 'king' in bio_lower:
            return 'King'
        elif 'queen' in bio_lower:
            return 'Queen'
        elif 'emperor' in bio_lower:
            return 'Emperor'
        elif 'empress' in bio_lower:
            return 'Empress'
        elif 'tsar' in bio_lower or 'czar' in bio_lower:
            return 'Tsar'

        return None

    @staticmethod
    def extract_dynasty(biography: str) -> Optional[str]:
        """
        Extract dynasty/house from biography text.

        Args:
            biography: Biography text

        Returns:
            Dynasty name if found, None otherwise
        """
        if not biography:
            return None

        bio_lower = biography.lower()
        for dynasty in BiographyParser.DYNASTIES:
            if dynasty.lower() in bio_lower:
                return dynasty

        return None

    @staticmethod
    def extract_context(biography: str) -> Tuple[Optional[str], Optional[str], Optional[str]]:
        """
        Extract all contextual information from biography.

        Args:
            biography: Biography text

        Returns:
            Tuple of (country, title, dynasty)
        """
        country = BiographyParser.extract_country(biography)
        title = BiographyParser.extract_royal_title(biography)
        dynasty = BiographyParser.extract_dynasty(biography)
        return country, title, dynasty
