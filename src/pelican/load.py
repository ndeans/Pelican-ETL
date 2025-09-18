# src/load.py

import re
from pathlib import Path
from typing import Dict


def _sanitize_filename(name: str) -> str:
    """
    Sanitize note title to be a safe filename.
    Replaces invalid characters with underscores.
    """
    return re.sub(r'[^a-zA-Z0-9_\-]+', "_", name)


def load_note(note: Dict[str, str], output_dir: str) -> None:
    """
    Load a single transformed note to disk as Markdown, or print if test mode is on.
    """
    title = note.get("title", "untitled")
    body = note.get("body", "")

    filename = _sanitize_filename(title) + ".md"
    filepath = Path(output_dir) / filename
    # breakpoint()

    if output_dir == "STDOUT":  # Test mode: print to console
        print(f"{'-'*40}\n# {title}\n\n{body}\n{'-'*40}")
    else:  # Normal mode: write to file
        filepath.write_text(f"# {title}\n\n{body}", encoding="utf-8")
        print(f"Saved note: {filepath}")
