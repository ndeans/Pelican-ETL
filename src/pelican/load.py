import re
from pathlib import Path
from .models import Note

def _sanitize_filename(name: str) -> str:
    """
    Sanitize a filename: keep alphanumerics, underscores, and dashes.
    """
    return re.sub(r'[^a-zA-Z0-9_\-]+', "_", name).strip("_")


def load_note(note: Note, output_dir: str) -> None:
    """
    Load a single Note to disk as Markdown.
    """
    title = note.title or "untitled"
    body = note.content or "(empty)"

    # Sanitize filename
    safe_title = _sanitize_filename(title)
    file_path = Path(output_dir) / f"{safe_title}.md"

    with file_path.open("w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n{body}")

    print(f"Saved note: {file_path}")

def load_note(note: Note, output_dir: str) -> None:
    """
    Load a single Note to disk as Markdown.
    """
    title = note.title or "untitled"
    body = note.content or "(empty)"

    # Sanitize filename
    safe_title = _sanitize_filename(title)
    file_path = Path(output_dir) / f"{safe_title}.md"

    with file_path.open("w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n{body}")

    print(f"Saved note: {file_path}")
