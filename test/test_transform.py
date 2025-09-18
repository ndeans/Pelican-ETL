import pytest
from pelican.transform import transform_note

def test_transform_plain_note():
    note = {
        "title": "Plain Note",
        "content": "This is a plain text note without XML tags."
    }
    result = transform_note(note)
    assert isinstance(result, dict)
    assert result["title"] == "Plain Note"
    assert result["body"] == "This is a plain text note without XML tags."

def test_transform_enml_with_bold():
    enml = """<?xml version="1.0" encoding="UTF-8"?>
    <en-note><b>bold text</b></en-note>"""
    note = {"title": "Bold Note", "content": enml}
    result = transform_note(note)
    assert result["body"] == "**bold text**"

def test_transform_enml_with_italic_and_link():
    enml = """<en-note>
        <i>italic text</i> and
        <a href="http://example.com">link</a>
    </en-note>"""
    note = {"title": "Italic & Link", "content": enml}
    result = transform_note(note)
    assert "*italic text*" in result["body"]
    assert "[link](http://example.com)" in result["body"]

def test_transform_enml_with_list():
    enml = """<en-note>
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
        </ul>
    </en-note>"""
    note = {"title": "List Note", "content": enml}
    result = transform_note(note)
    assert "- Item 1" in result["body"]
    assert "- Item 2" in result["body"]

def test_transform_enml_with_code_block():
    enml = """<en-note>
        <pre>print("hello")</pre>
    </en-note>"""
    note = {"title": "Code Note", "content": enml}
    result = transform_note(note)
    assert "```" in result["body"]
    assert 'print("hello")' in result["body"]



"""
    original...  
    note_md = transform_note(note)
    assert isinstance(note_md, dict)
    assert note_md["title"] == "Test Note"
    assert note_md["body"] == "This is a plain text note."
"""

