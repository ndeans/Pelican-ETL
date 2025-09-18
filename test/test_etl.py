import pytest, os
from pelican.extract import extract_notes
from pelican.transform import transform_note


def test_extract_sample():

    sample_file = "sample.enex"
    assert os.path.exists(sample_file), f"Missing {sample_file} for test."

    notes = extract_notes("sample.enex") 
    assert isinstance(notes, list)
    # We know sample.enex contains 1 note
    assert len(notes) >= 1

    note = notes[0]
    assert note["title"] == "Hello World"
    assert "sample Evernote export note" in note["content"]


def test_transform_sample():

    note = {
        "title": "Hello World",
        "content": "<content>This is a sample Evernote export note.</content>"
    }

    note_md = transform_note(note)

    assert isinstance(note_md, dict)

    assert note_md["title"] == "Hello World"
    assert note_md["body"] == "This is a sample Evernote export note."

