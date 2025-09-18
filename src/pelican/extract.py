import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Dict

def extract_notes(enex_path: str) -> List[Dict[str, str]]:
    """
    Parse an Evernote .enex file and return a list of notes.
    Each note is represented as a dict with keys: "title" and "content".
    """
    file_path = Path(enex_path)
    if not file_path.exists():
        raise FileNotFoundError(f"ENEX file not found: {enex_path}")

    tree = ET.parse(file_path)
    root = tree.getroot()

    notes: List[Dict[str, str]] = []
    for note in root.findall("note"):
        title = note.findtext("title", default="Untitled")
        content = note.findtext("content", default="")
        notes.append({"title": title, "content": content})

    return notes
