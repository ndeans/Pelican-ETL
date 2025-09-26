import xml.etree.ElementTree as ET
# from xml.etree import ElementTree as ET
from pathlib import Path
from typing import List, Dict
from .models import Note  # your dataclass module

def extract_from_enex(enex_path: str) -> List[Note]:
    
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
    
    with open(enml_path, 'r', encoding='utf-8') as f:
        content = f.read()
    root = ET.fromstring(content)

    body_html = ET.tostring(root, encoding='unicode', method='html')

    return [
        Note(
            title="Untitled ENML Note", 
            content=body_html,
            created="None",
            updated="None"
        )
    ]

'''
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
'''




