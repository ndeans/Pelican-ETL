# src/transform.py

def transform_note(note: dict) -> dict:
    """
    Dummy transformation function.
    Prepares the note for Obsidian (Markdown format).
    """
    transformed = {
        "title": note["title"],
        "body": f"# {note['title']}\n\n{note['content']}"
    }
    return transformed
