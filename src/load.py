# src/load.py

from pathlib import Path

def load_note(note: dict, vault_path: str):
    """
    Dummy load function.
    Writes note to a Markdown file in the given Obsidian vault.
    """
    vault = Path(vault_path)
    vault.mkdir(parents=True, exist_ok=True)
    file_path = vault / f"{note['title'].replace(':','-')}.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(note["body"])
    return file_path
