from dataclasses import dataclass

@dataclass
class Note:
    title: str
    content: str
    created: str = ""
    updated: str = ""
    # tags: list[str] = None
    # attachments: list[str] = None
    # Add other fields as necessary


