import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List
from .models import Note

def extract_from_enex(enex_path: str) -> List[Note]:
    """
    Extract multiple notes from an ENEX file.
    """
    file_path = Path(enex_path)
    if not file_path.exists():
        raise FileNotFoundError(f"ENEX file not found: {enex_path}")

    tree = ET.parse(file_path)
    root = tree.getroot()
    notes = []
    for note_elem in root.findall("note"):
        title = note_elem.findtext("title", default="Untitled")
        content = note_elem.findtext("content", default="")
        created = note_elem.findtext("created", default="")
        updated = note_elem.findtext("updated", default="")
        notes.append(Note(title=title, content=content, created=created, updated=updated))

    return notes

def extract_from_enml(enml_path: str) -> List[Note]:
    """
    Extract a single ENML note from a file (returning as a list for batch processing).
    """
    file_path = Path(enml_path)
    if not file_path.exists():
        raise FileNotFoundError(f"ENML file not found: {enml_path}")

    with file_path.open("r", encoding="utf-8") as f:
        content = f.read()

    return [
        Note(
            title="Untitled ENML Note",
            content=content,
            created="None",
            updated="None"
        )
    ]
