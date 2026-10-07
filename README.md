# MOD10 Machine Learning Project: Montreal Public Trees

Group project for MOD10 Introduction to Machine Learning (Concordia Continuing Education, Fall 2026), based on the City of Montreal public trees inventory.

## Setup

```bash
git clone git@github.com:Tezay/montreal-public-trees.git
cd montreal-public-trees
conda env create -f environment.yml
conda activate mod10
```

Then add the dataset as described in [data/README.md](data/README.md).

If conda raises `CondaToSNonInteractiveError`, accept the channel terms with the `conda tos accept` commands it prints. On the lab computers, first run `conda config --add envs_dirs "%USERPROFILE%\conda-envs"`.

## Layout

- `data/`: dataset snapshot (not versioned) and its documentation
- `notebooks/`: one notebook per deliverable, named `dNN_<topic>.ipynb`
- `src/mtl_trees/`: reusable code imported by the notebooks
- `tests/`: unit tests
- `reports/`: written deliverables and figures

## Development

```bash
pytest
ruff check . && ruff format .
```

Run notebooks top to bottom (Restart & Run All) before committing. Never commit data files and never edit `data/raw/`.
