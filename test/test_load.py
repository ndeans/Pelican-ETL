import io
import sys
import tempfile
from pathlib import Path

import pytest

from src.load import load_note


def test_load_note_test_mode(capsys):
    """Verify load_note prints correctly in test mode."""
    note = {"title": "Test Note", "body": "This is the body."}

    load_note(note, output_dir="unused", test=True)

    captured = capsys.readouterr()
    assert "# Test Note" in captured.out
    assert "This is the body." in captured.out
    assert "-" * 40 in captured.out


def test_load_note_file_output(tmp_path: Path):
    """Verify load_note writes a file when not in test mode."""
    note = {"title": "Test Dummy", "body": "This is a test dummy, dummy."}
    # breakpoint()
    load_note(note, output_dir=str(tmp_path), test=False)

    # Expect sanitized filename
    expected_file = tmp_path / "Test_Dummy.md"
    assert expected_file.exists()

    content = expected_file.read_text(encoding="utf-8")
    # assert "# My/Invalid:Title*" not in content  # title in file is unsanitized
    # assert "# My_Invalid_Title_" not in content  # sanitized not used in heading
    # assert "# My/Invalid:Title*" not in content  # heading is the original title
    assert "This is a test dummy, dummy." in content
