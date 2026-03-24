import sys
from pathlib import Path


def _ensure_project_root_in_path() -> None:
    project_root = Path(__file__).resolve().parent.parent
    root_str = str(project_root)
    if root_str not in sys.path:
        sys.path.insert(0, root_str)


_ensure_project_root_in_path()
