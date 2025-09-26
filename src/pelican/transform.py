import re
from typing import List, Dict
from pelican.models import Note  # your dataclass module

def transform_note(note: Note) -> Note:

    transformed_content = _enml_to_markdown(note.content)
    return Note(title=note.title, content=transformed_content)

def transform_notes(notes: List[Note]) -> List[Note]:
    """Transform a list of note dictionaries into Markdown."""
    return [transform_note(note) for note in notes]

def _enml_to_markdown(enml: str) -> str:
    """Convert ENML content to Markdown format."""
    return enml
