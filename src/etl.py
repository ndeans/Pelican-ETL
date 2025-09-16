# src/etl.py

import argparse
from src.extract import extract_note
from src.transform import transform_note
from src.load import load_note

def main():
    parser = argparse.ArgumentParser(description="Evernote → Obsidian ETL")
    parser.add_argument("enex_file", help="Path to the ENEX file")
    # parser.add_argument("--vault", default="vault", help="Obsidian vault path")
    parser.add_argument("--test", action="store_true", help="Use test vault")
    args = parser.parse_args()

    vault_path = "test_vault" if args.test else "vault"
    
    enex_file = "sample.enex"
    
    notes = extract_note(args.enex_file)
    for note in notes:
        note_md = transform_note(note)
        file_path = load_note(note_md, vault_path)
        print(f"Note written to {file_path}")

if __name__ == "__main__":
    main()
