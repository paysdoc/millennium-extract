"""
Supabase client and data fetching functions.
"""
import os
from typing import List, Dict
from dotenv import load_dotenv
from supabase import create_client, Client
from src.types.supabase_types import Character, Connection, DenormalizedConnection, CardData
from src.config import CATEGORY_ORDER


# Load environment variables
load_dotenv()


def get_supabase_client() -> Client:
    """Create and return a Supabase client."""
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url or not key:
        raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set in .env file")

    return create_client(url, key)


def fetch_all_characters(client: Client) -> List[Character]:
    """Fetch all characters from Supabase."""
    response = client.table("character").select("*").execute()

    characters = []
    for row in response.data:
        characters.append(Character(
            id=row['id'],
            name=row.get('name'),
            first_names=row.get('first_names'),
            birth_date=row.get('birth_date'),
            death_date=row.get('death_date'),
            biography=row.get('biography'),
            type=row.get('type'),
            link=row.get('link'),
            image_link=row.get('image_link'),
            joker_type=row.get('joker_type'),
            joker_type_value=row.get('joker_type_value'),
            joker_type_why=row.get('joker_type_why'),
            joker_type_why_short=row.get('joker_type_why_short')
        ))

    return characters


def fetch_character_by_name(client: Client, character_name: str) -> tuple[Character | None, List[Character]]:
    """
    Fetch a single character by name (case-insensitive).

    Args:
        client: Supabase client
        character_name: Name of the character to find

    Returns:
        Tuple of (exact_match, partial_matches)
        - exact_match: Character object if exact match found, None otherwise
        - partial_matches: List of Character objects that partially match the name
    """
    # Fetch all characters (needed for character_lookup in denormalization anyway)
    all_characters = fetch_all_characters(client)

    search_name = character_name.upper().strip()
    exact_match = None
    partial_matches = []

    for character in all_characters:
        char_name = (character.name or "").upper().strip()
        if char_name == search_name:
            exact_match = character
            break
        elif search_name in char_name:
            partial_matches.append(character)

    return exact_match, partial_matches


def fetch_connections_for_character(client: Client, character_id: int) -> List[Connection]:
    """Fetch all active connections where the character is either char1 or char2."""
    # Fetch connections where character is char1 and active=true
    response1 = client.table("connection").select("*").eq("char1_id", character_id).eq("active", True).execute()

    # Fetch connections where character is char2 and active=true
    response2 = client.table("connection").select("*").eq("char2_id", character_id).eq("active", True).execute()

    connections = []
    for row in response1.data + response2.data:
        connections.append(Connection(
            id=row['id'],
            char1_id=row.get('char1_id'),
            char2_id=row.get('char2_id'),
            value=row.get('value'),
            why=row.get('why'),
            why_short=row.get('why_short'),
            active=row.get('active')
        ))

    return connections


def denormalize_connections(
    client: Client,
    character_id: int,
    connections: List[Connection],
    character_lookup: Dict[int, Character]
) -> List[DenormalizedConnection]:
    """
    Replace character IDs with names in connections and add joker connections.

    Args:
        client: Supabase client
        character_id: ID of the current character
        connections: List of connections for the character
        character_lookup: Dictionary mapping character IDs to Character objects

    Returns:
        List of denormalized connections with character names, sorted by category then name
    """
    denormalized = []

    # Get the current character
    current_char = character_lookup.get(character_id)
    if not current_char:
        return denormalized

    current_category = current_char.type

    # Process regular connections
    for conn in connections:
        # Determine which character is the "other" character
        other_char_id = conn.char2_id if conn.char1_id == character_id else conn.char1_id

        if other_char_id is None or other_char_id not in character_lookup:
            continue

        other_char = character_lookup[other_char_id]

        denormalized.append(DenormalizedConnection(
            character_name=other_char.name or "Unknown",
            category_code=other_char.type or "Unknown",
            value=conn.value or 0,
            why=conn.why or "",
            why_short=conn.why_short
        ))

    # Add joker connections
    # Check all other characters to see if they have a joker_type matching current character's category
    for other_char_id, other_char in character_lookup.items():
        # Skip self
        if other_char_id == character_id:
            continue

        # Check if other character has a joker type
        if not other_char.joker_type:
            continue

        # Check if joker type matches current character's category (or is wildcard)
        if other_char.joker_type == "*" or other_char.joker_type == current_category:
            # Add joker connection
            denormalized.append(DenormalizedConnection(
                character_name=other_char.name or "Unknown",
                category_code=other_char.type or "Unknown",
                value=other_char.joker_type_value or 0,
                why=other_char.joker_type_why or "",
                why_short=other_char.joker_type_why_short
            ))

    # Sort by category (in specific order) then by name
    denormalized.sort(key=lambda x: (
        CATEGORY_ORDER.get(x.category_code, 99),  # Use 99 for unknown categories
        x.character_name.upper() if x.character_name else ""
    ))

    return denormalized


def fetch_card_data(client: Client, character: Character, character_lookup: Dict[int, Character]) -> CardData:
    """
    Fetch and prepare all data needed for a character card.

    Args:
        client: Supabase client
        character: Character to create card for
        character_lookup: Dictionary mapping character IDs to Character objects

    Returns:
        Complete CardData object ready for rendering
    """
    connections = fetch_connections_for_character(client, character.id)
    denormalized_connections = denormalize_connections(client, character.id, connections, character_lookup)

    return CardData(
        character=character,
        connections=denormalized_connections
    )


def fetch_single_card_data(client: Client, character_name: str) -> tuple[CardData | None, List[Character], int]:
    """
    Fetch card data for a single character by name.

    This is more efficient than fetch_all_card_data when you only need one character,
    as it still fetches all characters (needed for denormalization) but only processes
    connections for the requested character.

    Args:
        client: Supabase client
        character_name: Name of the character (case-insensitive)

    Returns:
        Tuple of (card_data, partial_matches, card_number)
        - card_data: CardData object if exact match found, None otherwise
        - partial_matches: List of Character objects that partially match the name
        - card_number: Position of character in alphabetical list (1-indexed), or 0 if not found
    """
    # Fetch all characters (needed for character_lookup in denormalization)
    all_characters = fetch_all_characters(client)

    # Create lookup dictionary
    character_lookup = {char.id: char for char in all_characters}

    # Find the specific character by name (case-insensitive)
    search_name = character_name.upper().strip()
    exact_match = None
    card_number = 0
    partial_matches = []

    for idx, character in enumerate(all_characters):
        char_name = (character.name or "").upper().strip()
        if char_name == search_name:
            exact_match = character
            card_number = idx + 1
            break
        elif search_name in char_name:
            partial_matches.append(character)

    if not exact_match:
        return None, partial_matches, 0

    # Fetch card data for the matched character
    card_data = fetch_card_data(client, exact_match, character_lookup)

    return card_data, [], card_number


def fetch_all_card_data(client: Client) -> List[CardData]:
    """
    Fetch data for all character cards, sorted by category then name.

    Returns:
        List of CardData objects sorted by category order (R, S, P, I, M, N, A, B, C, D, T)
        and then alphabetically by name within each category.
    """
    # Fetch all characters first
    characters = fetch_all_characters(client)

    # Sort characters by category order, then by name
    characters.sort(key=lambda char: (
        CATEGORY_ORDER.get(char.type, 99),  # Use 99 for unknown categories
        (char.name or "").upper()
    ))

    # Create lookup dictionary
    character_lookup = {char.id: char for char in characters}

    # Fetch card data for each character (already sorted)
    card_data_list = []
    for character in characters:
        card_data = fetch_card_data(client, character, character_lookup)
        card_data_list.append(card_data)

    return card_data_list
