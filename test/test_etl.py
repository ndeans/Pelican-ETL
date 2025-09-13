# test/test_etl.py
import pytest
from extract import extract_note
from transform import transform_note
from load import load_note
from pathlib import Path
import shutil

TEST_VAULT = "test_vault"

def setup_module(module):
    """Clean up test vault before tests"""
    vault_path = Path(TEST_VAULT)
    if vault_path.exists():
        shutil.rmtree(vault_path)

def test_full_etl():
    raw = "Hello Evernote"
    note = extract_note(raw)
    assert note["content"] == raw

    transformed = transform_note(note)
    assert transformed["body"].startswith("#")

    file_path = load_note(transformed, TEST_VAULT)
    assert Path(file_path).exists()
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "Hello Evernote" in content
