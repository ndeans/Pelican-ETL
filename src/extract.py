# src/extract.py
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Dict

def extract_note(enex_path: str) -> List[Dict[str, str]]:
    """
    Extract notes from an ENEX file into a list of dicts.
    Each dict contains 'title' and 'content'.

    Args:
        enex_path (str): Path to the ENEX file.
    Returns:
        List[Dict[str, str]]: Extracted notes.
    """

    file_path = Path(enex_path)
    if not file_path.exists():
        raise FileNotFoundError(f"ENEX file not found: {enex_path}")

    tree = ET.parse(file_path)
    root = tree.getroot()
    # ns = {"en": "http://xml.evernote.com/pub/enml2.dtd"}
    notes = []

    for note in root.findall("note"):
        title_elem = note.find("title")
        content_elem = note.find("content")

        title = title_elem.text if title_elem is not None else "Untitled"
        content = content_elem.text if content_elem is not None else ""

        notes.append({
            "title": title.strip(),
            "content": content.strip()              
        })

    return notes

    """
    Dummy extraction function.
    Simulates extracting a note from Evernote.
    
    return {
        "title": f"Note: {raw_input}",
        "content": raw_input
    }
    """

