# src/pelican/transform.py

from typing import List
from .models import Note

def transform_note(note: Note) -> Note:
    """
    Apply transformations to a single Note.
    Currently, this is a placeholder for ENML -> Markdown or other conversions.
    """
    # For now, just pass content through


    return Note(
        title=note.title,
        content=note.content,
        created=note.created,
        updated=note.updated
    )


def transform_notes(notes: List[Note]) -> List[Note]:
    """
    Transform a list of notes.
    """
    return [transform_note(note) for note in notes]
