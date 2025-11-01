#!/usr/bin/env python3
"""
Inspect Supabase database schema to verify table structures.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from src.supabase_client import get_supabase_client
import json


def inspect_table_schema(client, table_name):
    """Fetch a sample row to inspect the schema."""
    try:
        # Fetch one row to see all columns
        response = client.table(table_name).select("*").limit(1).execute()

        if response.data and len(response.data) > 0:
            sample_row = response.data[0]
            print(f"\n{'='*60}")
            print(f"Table: {table_name}")
            print(f"{'='*60}")
            print(f"Columns found ({len(sample_row)} total):")
            for key, value in sample_row.items():
                value_type = type(value).__name__
                value_preview = str(value)[:50] if value is not None else "None"
                print(f"  - {key:20s} : {value_type:10s} = {value_preview}")
            return sample_row
        else:
            print(f"\n{table_name}: No data found in table")
            return None
    except Exception as e:
        print(f"\nError inspecting {table_name}: {e}")
        return None


def main():
    print("Connecting to Supabase...")
    client = get_supabase_client()

    # Inspect character table
    char_sample = inspect_table_schema(client, "character")

    # Inspect connection table
    conn_sample = inspect_table_schema(client, "connection")

    # Get count of records
    print(f"\n{'='*60}")
    print("Record Counts")
    print(f"{'='*60}")

    try:
        char_count = client.table("character").select("id", count="exact").execute()
        print(f"Characters: {char_count.count}")
    except Exception as e:
        print(f"Error counting characters: {e}")

    try:
        conn_count = client.table("connection").select("id", count="exact").execute()
        print(f"Connections: {conn_count.count}")
    except Exception as e:
        print(f"Error counting connections: {e}")

    # Display full sample records in JSON format
    if char_sample:
        print(f"\n{'='*60}")
        print("Sample Character Record (JSON)")
        print(f"{'='*60}")
        print(json.dumps(char_sample, indent=2))

    if conn_sample:
        print(f"\n{'='*60}")
        print("Sample Connection Record (JSON)")
        print(f"{'='*60}")
        print(json.dumps(conn_sample, indent=2))


if __name__ == "__main__":
    main()
