"""Make student notebooks from solution notebooks.

Code cells tagged `solution` are replaced by a placeholder. Markdown cells
tagged `solution` are removed. Every output is cleared.

Usage: python tools/strip_solutions.py [notebook.ipynb ...]
With no arguments, every practicals/*.ipynb is processed.
Output: practicals/student/<same file name>.
"""
import json
import sys
from pathlib import Path

PLACEHOLDER = "# YOUR CODE HERE\n...\n"


def _tags(cell):
    return cell.get("metadata", {}).get("tags", [])


def strip(nb: dict) -> dict:
    cells = []
    for cell in nb["cells"]:
        if "solution" in _tags(cell):
            if cell["cell_type"] != "code":
                continue
            cell = {**cell, "source": PLACEHOLDER}
        if cell["cell_type"] == "code":
            cell = {**cell, "outputs": [], "execution_count": None}
        cells.append(cell)
    return {**nb, "cells": cells}


def main(paths):
    paths = [Path(p) for p in paths] or sorted(Path("practicals").glob("*.ipynb"))
    for path in paths:
        out = strip(json.loads(path.read_text()))
        leaked = [c for c in out["cells"] if "solution" in _tags(c) and c["source"] != PLACEHOLDER]
        assert not leaked, f"{path}: solution text survived"
        dest = path.parent / "student" / path.name
        dest.parent.mkdir(exist_ok=True)
        dest.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
        n = sum("solution" in _tags(c) for c in out["cells"])
        print(f"{path} -> {dest} ({n} solution cells blanked)")


if __name__ == "__main__":
    main(sys.argv[1:])
