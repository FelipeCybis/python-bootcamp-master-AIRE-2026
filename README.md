# Python bootcamp, part 2: arrays, plots, tables

Part 2 of the Python bootcamp of the
[M1 AIRE master](https://master.learningplanetinstitute.org/en/m1-aire) at
the Learning Planet Institute. Two lectures and two practicals take the
students from lists and loops to NumPy arrays, plots, a bit of pandas, and a
some linear regression. The bootcamp prepares them for statistics and data
science courses that follows. Slides are Quarto `revealjs`  rendered directly
from Jupyter notebooks. All data comes from one open dataset: a rat walking in
an arena during functional ultrasound imaging (Cybis Pereira et al., Cell
Reports 2026, OSF project 2v6f7, CC-BY 4.0). Every notebook downloads the
files it needs on first run.

## Teacher setup

1. Install [uv](https://docs.astral.sh/uv/) and [Quarto](https://quarto.org/docs/get-started/) (1.4 or newer).
2. `uv sync` builds `.venv/` from `uv.lock`.

## Render the slides

```bash
uv run quarto render                                   # all decks -> _site/
uv run quarto preview lectures/01_arrays.ipynb         # one deck, live reload
```

Each lecture notebook produces two files in `_site/lectures/`:
`<name>-slides.html` (the deck) and `<name>.html` (a handout with a table of
contents). Cells are executed at render time, so the first render downloads
the data into `lectures/data/`.

Slide rules: a `##` heading starts a slide, a `#` heading starts a section.
Shared deck options are in `lectures/_metadata.yml`; each notebook sets its
own `output-file` in its first raw cell.

## Practicals

`practicals/*.ipynb` are the solutions. Cells tagged `solution` become
`# YOUR CODE HERE` in the student versions:

```bash
uv run python tools/strip_solutions.py                 # writes practicals/student/
uv run python tools/test_strip_solutions.py            # one check for the converter
```

To refresh stored outputs in a solution notebook:

```bash
uv run jupyter nbconvert --ExecutePreprocessor.timeout=600 --to notebook --execute --inplace practicals/01_where_did_the_rat_go.ipynb
```

## Student setup

Choose one:

- `uv sync`, then `uv run jupyter lab`.
- `pip install -r requirements.txt` inside a virtual environment.
- Open the notebook in Google Colab. Nothing to install.

The data downloads itself (about 60 MB, once per folder).

## Layout

- `lectures/` lecture notebooks and `_metadata.yml`
- `practicals/` solution notebooks; `practicals/student/` generated versions
- `tools/` helper scripts
