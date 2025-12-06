from pathlib import Path

def read_lines(path: Path) -> list[str]:
    """Read a file into a list of lines (stripped of trailing newlines)."""
    return path.read_text().splitlines()

