"""Small JSON-file storage helpers shared by SkillMatch feature areas."""

import json
import os
import tempfile
from pathlib import Path
from typing import Any


DATA_DIR = Path(__file__).resolve().parent / "data"


def _file_path(filename: str) -> Path:
    """Return a safe JSON filename contained directly in the shared data folder."""
    if not filename or Path(filename).name != filename or Path(filename).suffix != ".json":
        raise ValueError("Use a simple .json filename stored in the data directory.")
    return DATA_DIR / filename


def load(filename: str) -> Any:
    """Load a JSON file, returning an empty object when it has not been created yet."""
    path = _file_path(filename)
    if not path.exists():
        return {}

    with path.open("r", encoding="utf-8") as data_file:
        return json.load(data_file)


def save(filename: str, data: Any) -> None:
    """Save JSON through a temporary file so interrupted writes do not corrupt data."""
    path = _file_path(filename)
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    file_descriptor, temporary_name = tempfile.mkstemp(
        dir=DATA_DIR,
        prefix=f".{path.name}.",
        suffix=".tmp",
    )
    try:
        with os.fdopen(file_descriptor, "w", encoding="utf-8") as data_file:
            json.dump(data, data_file, indent=2, ensure_ascii=False)
            data_file.write("\n")
        os.replace(temporary_name, path)
    finally:
        Path(temporary_name).unlink(missing_ok=True)
