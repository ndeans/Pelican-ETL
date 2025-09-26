import argparse
from pathlib import Path
from pelican.extract import extract_from_enex, extract_from_enml    
from pelican.transform import transform_notes
from pelican.load import load_note

def run_etl(file_path: str, output_dir: str) -> None:

    fmt = detect_format(file_path=file_path)
    
    # Extract
    if fmt == "enex":
        notes = extract_from_enex(file_path)
    elif fmt == "enml":
        notes = extract_from_enml(file_path)
    else:
        raise ValueError(f"Unsupported file format: {fmt}")

    # Transform and Load
    transformed_notes = transform_notes(notes)

    for note in transformed_notes:
        load_note(note, output_dir)

def detect_format(file_path: str) -> str:
    
    with open(file_path, 'r', encoding='utf-8') as file:
        first_kb = file.read(2048).lower()
    if "<en-export" in first_kb:
            return "enex"
    elif "<en-note" in first_kb:
        return "enml"
    else:
        raise ValueError(f"Unsupported file format: Expecting ENEX or ENML")


def main():
    parser = argparse.ArgumentParser(description="ETL pipeline for Evernote ENEX export")
    parser.add_argument("enex_path", help="Path to Evernote .enex file")
    parser.add_argument("--vault", default="vault", help="Directory to save Markdown files")
    parser.add_argument("--test", action="store_true", help="Print transformed notes instead of saving")
    args = parser.parse_args()

    # breakpoint()
 
    vault_dir = "test_vault" if args.test else args.vault
    output_dir = Path(vault_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    run_etl(args.enex_path, str(output_dir))
       

if __name__ == "__main__":
    main()
