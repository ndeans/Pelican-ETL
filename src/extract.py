# src/extract.py

def extract_note(raw_input: str) -> dict:
    """
    Dummy extraction function.
    Simulates extracting a note from Evernote.
    """
    return {
        "title": f"Note: {raw_input}",
        "content": raw_input
    }
