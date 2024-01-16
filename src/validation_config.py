"""
Script to load validation config yaml file
"""
from dataclasses import dataclass
from pathlib import Path
from typing import List

import yaml


@dataclass
class DataConfig:
    """
    Dataclass to store information about a table
    """
    name: str
    version: str
    filename: Path = None
    sheet_id: str = None
    gid: str = None


@dataclass
class ValidationConfig:
    """
    Dataclass to store validation configuration
    """
    relationships: dict
    data: List[DataConfig]

    def __post_init__(self):
        info_data = []
        for table in self.data:
            info_data.append(DataConfig(**table))
        self.data = info_data


def load_validation_config(config_file: Path) -> ValidationConfig:
    """
    Load validation-config.yml to ValidationConfig dataclass
    """
    with open(config_file, mode="r", encoding="utf-8") as file:
        config = file.read()
    config = yaml.load(config, Loader=yaml.SafeLoader)
    return ValidationConfig(**config)
