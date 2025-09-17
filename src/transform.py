import re
from typing import List, Dict

def transform_note(note: dict) -> dict:
    """Convert Evernote ENML/plain content into Markdown without external libs."""

    raw = note.get("content", "")

    # Drop Evernote wrapper tags
    raw = re.sub(r"</?(content|en-note)>", "", raw, flags=re.IGNORECASE).strip()

    # Inline replacements
    raw = re.sub(r"<b>(.*?)</b>", r"**\1**", raw, flags=re.DOTALL|re.IGNORECASE)
    raw = re.sub(r"<i>(.*?)</i>", r"*\1*", raw, flags=re.DOTALL|re.IGNORECASE)
    raw = re.sub(r'<a href="(.*?)">(.*?)</a>', r"[\2](\1)", raw, flags=re.DOTALL|re.IGNORECASE)

    # Code blocks
    raw = re.sub(r"<pre>(.*?)</pre>", r"```\n\1\n```", raw, flags=re.DOTALL|re.IGNORECASE)

    # Lists
    raw = re.sub(r"<ul>\s*(.*?)\s*</ul>", r"\1", raw, flags=re.DOTALL|re.IGNORECASE)
    raw = re.sub(r"<li>\s*(.*?)\s*</li>", r"- \1\n", raw, flags=re.DOTALL|re.IGNORECASE)

    # Remove any remaining tags
    raw = re.sub(r"<[^>]+>", "", raw)

    body = raw.strip()

    return {
        "title": note.get("title", "Untitled"),
        "body": body
    }

def transform_notes(notes: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Transform a list of note dictionaries into Markdown."""
    return [transform_note(note) for note in notes]
