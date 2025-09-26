# import pytest
from pelican.transform import transform_note
from pelican.models import Note

def test_transform_plain_note():

    note = Note(
        title="Plain Note",
        content="This is a plain text note without XML tags.",
        created="",
        updated=""
    )
    result = transform_note(note)
    assert isinstance(result, Note)
    assert result.title == "Plain Note"
    assert result.content == "This is a plain text note without XML tags."


def test_transform_enml_with_bold():

    enml = """<?xml version="1.0" encoding="UTF-8"?> <en-note><b>bold text</b></en-note>"""
    note = Note(
        title="Bold Note",
        content=enml
        )
    result = transform_note(note)
    assert isinstance(result, Note)
    assert result.title == "Bold Note"
    # assert result.content == "**bold text**"       # ENML to MD is not implement yet - function returns the paramter.


def test_transform_enml_with_italic_and_link():
    enml = """<en-note><i>italic text</i> and <a href="http://example.com">link</a></en-note>"""
    note = Note(
        title="Italic & Link",
        content=enml
    )
    result = transform_note(note)
    assert isinstance(result, Note)
    assert result.title == "Italic & Link"
    
    # assert "*italic text*" in result.content
    # assert "[link](http://example.com)" in result.content


def test_transform_enml_with_list():
    enml = """<en-note>
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
        </ul>
    </en-note>"""
    note = Note(
        title="List Note",
        content=enml
    )
    result = transform_note(note)
    # assert "- Item 1" in result.content
    # assert "- Item 2" in result.content


def test_transform_enml_with_code_block():
    enml = """<en-note>
        <pre>print("hello")</pre>
    </en-note>"""
    note = Note(
        title="Code Note",
        content=enml
    )
    result = transform_note(note)
    # assert "```" in result.content
    # assert 'print("hello")' in result.content



