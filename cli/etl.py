# cli/etl.py

import sys
from pathlib import Path

# Ensure 'src' directory is on sys.path no matter where we're launched from
project_root = Path(__file__).resolve().parents[1]
src_path = project_root / "src"
for p in (project_root, src_path):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))


# if str(src_path) not in sys.path:
#     sys.path.insert(0, str(src_path))

# --- Diagnostic output ---
print("\n[Pelican-ETL Debug Info]")
print(f"Running from: {Path.cwd()}")
print("Python executable:", sys.executable)
print("sys.path:")
for p in sys.path:
    print("   ", p)
print()

import argparse
from src.pelican.extract import extract_from_enex, extract_from_enml
from src.pelican.transform import transform_notes
from src.pelican.load import load_note
from src.pelican.models import Note
from typing import List

def detect_format(file_path: str) -> str:
    """
    Simple format detection based on file extension.
    """
    ext = Path(file_path).suffix.lower()
    if ext == ".enex":
        return "enex"
    elif ext == ".enml":
        return "enml"
    else:
        raise ValueError(f"Unsupported file extension: {ext}")


def run_etl(input_file: str, output_vault: str, fmt: str = None) -> None:
    """
    Main ETL loop:
    1. Detect format (or validate user-specified format)
    2. Extract notes
    3. Transform notes
    4. Load notes
    """

    input_path = Path(input_file)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    # Determine format
    if fmt is None:
        fmt = detect_format(input_file)
    else:
        detected_fmt = detect_format(input_file)
        if detected_fmt != fmt:
            raise ValueError(f"Input file format '{detected_fmt}' does not match specified format '{fmt}'")

    # Extract
    if fmt == "enex":
        notes: List[Note] = extract_from_enex(input_file)
    elif fmt == "enml":
        notes: List[Note] = extract_from_enml(input_file)
    else:
        raise ValueError(f"Unsupported format: {fmt}")

    if not notes:
        print("No notes extracted. Exiting.")
        return

    output_dir = Path(output_vault)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Transform & Load loop
    for note in notes:
        transformed_list = transform_notes([note])  # returns a list of Note(s)
        for transformed_note in transformed_list:
            load_note(transformed_note, str(output_dir))


def main():
    parser = argparse.ArgumentParser(description="Pelican ETL CLI")
    parser.add_argument("--input", help="Path to input ENEX or ENML file")
    parser.add_argument("--vault", "-v", default="vault", help="Output directory / vault")
    parser.add_argument("--format", "-f", choices=["enex", "enml"], help="Force input format")

    args = parser.parse_args()

    run_etl(args.input, args.vault, args.format)


if __name__ == "__main__":
    main()
