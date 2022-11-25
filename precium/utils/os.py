from pathlib import Path


def create_dir_if_not_exists(path: Path) -> None:
    if not path.exists():
        path.mkdir()
