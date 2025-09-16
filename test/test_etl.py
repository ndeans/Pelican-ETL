import os
from src.extract import extract_note

def test_extract_sample():
    sample_file = "sample.enex"
    assert os.path.exists(sample_file), f"Missing {sample_file} for test."

    notes = extract_note(sample_file)

    # We know sample.enex contains 1 note
    assert len(notes) == 1

    note = notes[0]
    assert note["title"] == "Hello World"
    assert "sample Evernote export note" in note["content"]


