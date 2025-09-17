import argparse
from pathlib import Path

from src.extract import extract_notes
from src.transform import transform_notes
from src.load import load_note


def run_etl(enex_path: str, output_dir: str, test: bool = False) -> None:
    """
    Run the ETL pipeline for Evernote .enex files.
    """
    # Extract
    notes = extract_notes(enex_path)

    # Transform
    transformed_notes = transform_notes(notes)

    # Load
    for note in transformed_notes:
        load_note(note, output_dir, test)


def main():
    parser = argparse.ArgumentParser(description="ETL pipeline for Evernote ENEX export")
    parser.add_argument("enex_path", help="Path to Evernote .enex file")
    parser.add_argument("--output-dir", default="output", help="Directory to save Markdown files")
    parser.add_argument("--test", action="store_true", help="Print transformed notes instead of saving")

    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    run_etl(args.enex_path, str(output_dir), args.test)


if __name__ == "__main__":
    main()
