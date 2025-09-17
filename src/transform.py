# src/transform.py
from bs4 import BeautifulSoup
import re
from typing import Dict

def _enml_to_markdown(enml: str) -> str:
    """
    Convert an ENML/XHTML fragment into plain-ish Markdown text.
    This is a simple conversion for common elements; extend as needed.
    """
    soup = BeautifulSoup(enml, "xml")

    # If Evernote wraps content in <en-note>, prefer that subtree
    en_note = soup.find("en-note")
    target = en_note if en_note is not None else soup

    # Bold, italic, underline
    for b in target.find_all("b"):
        b.replace_with(f"**{b.get_text()}**")
    for i in target.find_all("i"):
        i.replace_with(f"*{i.get_text()}*")
    for u in target.find_all("u"):
        u.replace_with(f"_{u.get_text()}_")

    # Code blocks / pre
    for pre in target.find_all("pre"):
        code_text = pre.get_text()
        pre.replace_with(f"\n```\n{code_text}\n```\n")

    # Links
    for a in target.find_all("a"):
        href = a.get("href") or a.get("href") or ""
        a.replace_with(f"[{a.get_text()}]({href})")

    # Lists (simple - flattens nesting)
    for li in target.find_all("li"):
        parent = li.find_parent()
        prefix = "1. " if parent and parent.name == "ol" else "- "
        li.replace_with(f"{prefix}{li.get_text()}\n")

    # Finally extract text with reasonable separators
    text = target.get_text("\n")
    # Collapse multiple blank lines
    text = re.sub(r"\n\s*\n+", "\n\n", text).strip()
    return text

def transform_note(note: Dict[str, str]) -> Dict[str, str]:
    """
    Input: note dict with keys 'title' and 'content'
    Output: dict with 'title' and 'body' (Markdown-ready string)
    """
    if not isinstance(note, dict):
        raise TypeError("transform_note expects a dict with 'title' and 'content'")

    title = note.get("title", "Untitled")
    content = note.get("content", "") or ""
    content_stripped = content.strip()

    # Heuristic: if content looks like XML/ENML (has tags or XML declaration), parse it.
    looks_like_xml = content_stripped.startswith("<?xml") or ("<" in content_stripped and ">" in content_stripped)
    if looks_like_xml:
        try:
            body = _enml_to_markdown(content_stripped)
        except Exception:
            # If parsing fails for any reason, fallback to the raw text
            body = content_stripped
    else:
        # plain-text note body — no XML parsing needed
        body = content_stripped

    return {
        "title": title,
        "body": body
    }
