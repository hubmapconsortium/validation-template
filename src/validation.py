from .validation_config import load_validation_config
from pathlib import Path


def validate(configfile: Path):
    config = load_validation_config(configfile)
