# src/etl.py

import argparse
from extract import extract_note
from transform import transform_note
from load import load_note

def main():
    parser = argparse.ArgumentParser(description="Evernote → Obsidian ETL")
    parser.add_argument("input", help="Raw note content or file")
    parser.add_argument("--vault", default="vault", help="Obsidian vault path")
    parser.add_argument("--test", action="store_true", help="Use test vault")
    args = parser.parse_args()

    vault = "test_vault" if args.test else args.vault

    note = extract_note(args.input)
    note_md = transform_note(note)
    file_path = load_note(note_md, vault)

    print(f"Note written to {file_path}")


if __name__ == "__main__":
    main()
