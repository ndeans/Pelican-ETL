from src.pelican.transform import transform_note, transform_notes
from src.pelican.models import Note

def test_transform_note():
    note = Note(title="Test Note", content="Some content", created="2025", updated="2025")
    result = transform_note(note)
    assert isinstance(result, Note)
    assert result.title == "Test Note"
    assert result.content == "Some content"

def test_transform_notes():
    notes = [
        Note(title="Note 1", content="Content 1", created="2025", updated="2025"),
        Note(title="Note 2", content="Content 2", created="2025", updated="2025"),
    ]
    results = transform_notes(notes)
    assert isinstance(results, list)
    assert len(results) == 2
    for original, transformed in zip(notes, results):
        assert transformed.title == original.title
        assert transformed.content == original.content





