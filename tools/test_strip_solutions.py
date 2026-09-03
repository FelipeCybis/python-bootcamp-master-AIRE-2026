"""One check for strip_solutions. Run: uv run python tools/test_strip_solutions.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from strip_solutions import PLACEHOLDER, strip


def cell(kind, src, tags=(), outputs=None):
    c = {"cell_type": kind, "metadata": {"tags": list(tags)}, "source": src}
    if kind == "code":
        c["outputs"] = outputs or []
        c["execution_count"] = 3
    return c


nb = {
    "cells": [
        cell("markdown", "## Exercise 1"),
        cell("code", "x = 42", tags=["solution"], outputs=[{"output_type": "stream", "text": "hi"}]),
        cell("markdown", "The answer is 42.", tags=["solution"]),
        cell("code", "assert x == 42", outputs=[{"output_type": "stream", "text": "ok"}]),
    ],
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 5,
}

out = strip(nb)
assert [c["cell_type"] for c in out["cells"]] == ["markdown", "code", "code"]
assert out["cells"][1]["source"] == PLACEHOLDER
assert out["cells"][2]["source"] == "assert x == 42"
assert all(c["outputs"] == [] and c["execution_count"] is None for c in out["cells"] if c["cell_type"] == "code")
assert nb["cells"][1]["source"] == "x = 42", "input notebook must not be mutated"
print("ok")
