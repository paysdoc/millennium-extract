"""
Supabase client and data fetching functions.
"""
import os
from typing import List, Dict
from dotenv import load_dotenv
from supabase import create_client, Client
from src.types.supabase_types import Character, Connection, DenormalizedConnection, CardData


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
            image_link=row.get('image_link')
        ))

    return characters


def fetch_connections_for_character(client: Client, character_id: int) -> List[Connection]:
    """Fetch all connections where the character is either char1 or char2."""
    # Fetch connections where character is char1
    response1 = client.table("connection").select("*").eq("char1_id", character_id).execute()

    # Fetch connections where character is char2
    response2 = client.table("connection").select("*").eq("char2_id", character_id).execute()

    connections = []
    for row in response1.data + response2.data:
        connections.append(Connection(
            id=row['id'],
            char1_id=row.get('char1_id'),
            char2_id=row.get('char2_id'),
            value=row.get('value'),
            why=row.get('why')
        ))

    return connections


def denormalize_connections(
    client: Client,
    character_id: int,
    connections: List[Connection],
    character_lookup: Dict[int, Character]
) -> List[DenormalizedConnection]:
    """
    Replace character IDs with names in connections.

    Args:
        client: Supabase client
        character_id: ID of the current character
        connections: List of connections for the character
        character_lookup: Dictionary mapping character IDs to Character objects

    Returns:
        List of denormalized connections with character names
    """
    denormalized = []

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
            why=conn.why or ""
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


def fetch_all_card_data(client: Client) -> List[CardData]:
    """Fetch data for all character cards."""
    # Fetch all characters first
    characters = fetch_all_characters(client)

    # Create lookup dictionary
    character_lookup = {char.id: char for char in characters}

    # Fetch card data for each character
    card_data_list = []
    for character in characters:
        card_data = fetch_card_data(client, character, character_lookup)
        card_data_list.append(card_data)

    return card_data_list
