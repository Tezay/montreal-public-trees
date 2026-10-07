"""Project-wide paths and constants."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
REPORTS = PROJECT_ROOT / "reports"

RAW_TREES_CSV = DATA_RAW / "montreal_public_trees_2026-10-07.csv"

RANDOM_SEED = 42
