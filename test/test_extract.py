import os
import tempfile
from pathlib import Path
import pytest
from pelican.extract import extract_from_enex, extract_from_enml
from pelican.models import Note


def test_extract_from_enex_single_note():
    sample_file = "sample.enex"
    assert os.path.exists(sample_file), f"Missing {sample_file} for test."

    notes = extract_from_enex(sample_file)

    assert isinstance(notes, list)
    assert len(notes) >= 1

    first = notes[0]
    assert isinstance(first, Note)
    assert first.title == "Hello World"
    assert "sample Evernote export note" in first.content
    assert hasattr(first, "created")
    assert hasattr(first, "updated")


def test_extract_from_enml_temporary_file():
    enml_content = """<?xml version="1.0" encoding="UTF-8"?>
<en-note>
  <div>Hello <b>World</b> from ENML</div>
</en-note>
"""
    with tempfile.NamedTemporaryFile("w+", suffix=".enml", delete=False, encoding="utf-8") as tmp:
        tmp.write(enml_content)
        tmp.flush()
        tmp_path = Path(tmp.name)

    try:
        notes = extract_from_enml(str(tmp_path))

        assert isinstance(notes, list)
        assert len(notes) == 1

        note = notes[0]
        assert isinstance(note, Note)
        assert "Hello" in note.content
        assert "World" in note.content
        assert note.title == "Untitled ENML Note"
        assert note.created == "None"
        assert note.updated == "None"
    finally:
        tmp_path.unlink(missing_ok=True)
