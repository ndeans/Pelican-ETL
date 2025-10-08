from pathlib import Path
from src.pelican.load import load_note, _sanitize_filename
from src.pelican.models import Note

def test_load_note_file_output(tmp_path):
    note = Note(title="My/Invalid:Title*", content="File content here.", created="2025", updated="2025")
    load_note(note, str(tmp_path))

    expected_file = tmp_path / "My_Invalid_Title.md"
    assert expected_file.exists()
    content = expected_file.read_text(encoding="utf-8")
    # The file should contain the original title in the Markdown header
    assert f"# {note.title}" in content
    assert "File content here." in content

def test_load_multiple_notes(tmp_path: Path):
    """
    Verify that multiple notes are written to disk correctly.
    """
    notes = [
        Note(title="First Note", content="Content 1", created="2025", updated="2025"),
        Note(title="Second Note", content="Content 2", created="2025", updated="2025"),
    ]

    # Save each note
    for note in notes:
        load_note(note, str(tmp_path))

    # Verify that each file exists using the same sanitization as load_note
    for note in notes:
        safe_title = _sanitize_filename(note.title)
        file_path = tmp_path / f"{safe_title}.md"
        assert file_path.exists(), f"Expected file {file_path} not found"

        # Optionally, check the content
        content = file_path.read_text(encoding="utf-8")
        assert note.content in content


