import os
from pathlib import Path
from src.pelican.extract import extract_from_enex, extract_from_enml
from src.pelican.models import Note

def test_extract_from_enex():
    sample_file = "data/sample.enex"
    assert os.path.exists(sample_file), f"Missing {sample_file} for test."

    notes = extract_from_enex(sample_file)
    assert isinstance(notes, list)
    assert len(notes) >= 1
    assert all(isinstance(n, Note) for n in notes)

    note = notes[0]
    assert note.title == "Hello World"
    assert "sample Evernote export note" in note.content

def test_extract_from_enml(tmp_path):
    enml_file = tmp_path / "sample.enml"
    enml_file.write_text("<en-note><b>Bold ENML</b></en-note>", encoding="utf-8")

    notes = extract_from_enml(str(enml_file))
    assert isinstance(notes, list)
    assert len(notes) == 1
    note = notes[0]
    assert isinstance(note, Note)
    assert "Bold ENML" in note.content
