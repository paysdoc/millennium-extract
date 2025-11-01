#!/usr/bin/env python3
"""
Millennium Card Producer CLI
Generate printable PDF cards for Millennium game characters.
"""
import sys
from pathlib import Path

# Add parent directory to path to allow imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import click
from src.supabase_client import get_supabase_client, fetch_all_card_data
from src.cards import generate_cards_pdf, generate_single_card_pdf


@click.group()
def cli():
    """Millennium Card Producer - Generate printable character cards."""
    pass


@cli.command()
@click.option(
    '--output',
    '-o',
    default='millennium_cards.pdf',
    help='Output PDF file path'
)
@click.option(
    '--fronts-only',
    is_flag=True,
    help='Generate only card fronts (no backs)'
)
def generate_all(output: str, fronts_only: bool):
    """
    Generate PDF with all character cards from Supabase.

    This command fetches all characters and their connections from Supabase,
    denormalizes the data, and generates a printable PDF with card fronts
    and backs arranged for double-sided printing.
    """
    try:
        click.echo("Connecting to Supabase...")
        client = get_supabase_client()

        click.echo("Fetching character data...")
        card_data_list = fetch_all_card_data(client)

        if not card_data_list:
            click.echo("No characters found in database.", err=True)
            return

        click.echo(f"Found {len(card_data_list)} characters")

        click.echo(f"Generating PDF: {output}")
        generate_cards_pdf(card_data_list, output, fronts_only=fronts_only)

        click.echo(click.style("✓ Cards generated successfully!", fg='green'))

    except Exception as e:
        click.echo(click.style(f"Error: {str(e)}", fg='red'), err=True)
        raise click.Abort()


@cli.command()
@click.argument('character_id', type=int)
@click.option(
    '--output',
    '-o',
    default='millennium_card_preview.pdf',
    help='Output PDF file path'
)
def generate_single(character_id: int, output: str):
    """
    Generate a preview PDF for a single character card.

    Shows front and back side by side on one page.

    Arguments:
        character_id: The ID of the character to generate a card for
    """
    try:
        click.echo(f"Connecting to Supabase...")
        client = get_supabase_client()

        click.echo(f"Fetching data for character ID {character_id}...")
        all_card_data = fetch_all_card_data(client)

        # Find the specific character
        card_data = None
        card_number = 0
        for idx, data in enumerate(all_card_data):
            if data.character.id == character_id:
                card_data = data
                card_number = idx + 1
                break

        if not card_data:
            click.echo(f"Character with ID {character_id} not found.", err=True)
            return

        click.echo(f"Generating preview PDF: {output}")
        generate_single_card_pdf(card_data, output, card_number)

        click.echo(click.style("✓ Card preview generated successfully!", fg='green'))

    except Exception as e:
        click.echo(click.style(f"Error: {str(e)}", fg='red'), err=True)
        raise click.Abort()


@cli.command()
@click.option(
    '--sort-by',
    '-s',
    default='id',
    type=click.Choice(['id', 'name', 'category', 'birth_date', 'death_date', 'connections'], case_sensitive=False),
    help='Primary sort field (default: id)'
)
@click.option(
    '--sort-by-2',
    '-s2',
    default=None,
    type=click.Choice(['id', 'name', 'category', 'birth_date', 'death_date', 'connections'], case_sensitive=False),
    help='Secondary sort field (optional)'
)
@click.option(
    '--reverse',
    '-r',
    is_flag=True,
    help='Reverse sort order (descending)'
)
def list_characters(sort_by: str, sort_by_2: str, reverse: bool):
    """
    List all characters in the database.

    Examples:
        List sorted by category, then name:
        $ python src/main.py list-characters -s category -s2 name

        List sorted by connections (descending):
        $ python src/main.py list-characters -s connections -r

        List sorted by birth date:
        $ python src/main.py list-characters -s birth_date
    """
    try:
        click.echo("Connecting to Supabase...")
        client = get_supabase_client()

        click.echo("Fetching characters...")
        card_data_list = fetch_all_card_data(client)

        if not card_data_list:
            click.echo("No characters found in database.")
            return

        # Create sorting key function
        def get_sort_key(data):
            char = data.character
            keys = []

            for field in [sort_by, sort_by_2]:
                if field is None:
                    continue

                if field == 'id':
                    keys.append(char.id)
                elif field == 'name':
                    keys.append((char.name or "").lower())
                elif field == 'category':
                    keys.append(char.type or "")
                elif field == 'birth_date':
                    keys.append(char.birth_date or "")
                elif field == 'death_date':
                    keys.append(char.death_date or "")
                elif field == 'connections':
                    keys.append(len(data.connections))

            return tuple(keys)

        # Sort the data
        sorted_data = sorted(card_data_list, key=get_sort_key, reverse=reverse)

        # Display sort information
        sort_info = f"Sorted by: {sort_by}"
        if sort_by_2:
            sort_info += f", then {sort_by_2}"
        if reverse:
            sort_info += " (descending)"

        click.echo(f"\nFound {len(sorted_data)} characters")
        click.echo(f"{sort_info}\n")

        for idx, data in enumerate(sorted_data, 1):
            char = data.character
            category = char.type or "?"
            name = char.name or "Unknown"
            dates = f"{char.birth_date or '?'}-{char.death_date or '?'}"
            connections = len(data.connections)

            click.echo(
                f"{idx:3d}. [{category}] {name:30s} ({dates}) - {connections} connections"
            )

    except Exception as e:
        click.echo(click.style(f"Error: {str(e)}", fg='red'), err=True)
        raise click.Abort()


if __name__ == '__main__':
    cli()
