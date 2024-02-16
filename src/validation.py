"""
Main script to run workflow for each data in config file
"""
import argparse
import os
from pathlib import Path

import pandas as pd
from asct_parser.asct_parser import parse_asctb
from asct_parser.utils.util import load_asctb
from relation_validator.utils.utils import (get_labels, get_obograph,
                                            save_obograph)
from relation_validator.validator import run_validation

from config.validation_config import load_validation_config


def validate(configfile: Path):
    config = load_validation_config(configfile)

    output_dir = os.path.join("output")

    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    for d in config.data:
        data_dir = os.path.join(output_dir, d.name)

        if not os.path.isdir(data_dir):
            os.mkdir(data_dir)

        if d.sheet_id and d.gid:
            asct_parsed = parse_asctb(
                load_asctb(gid=d.gid, sheet_id=d.sheet_id)
            )
            temp_filename = f"{d.name}-{d.version}"

        if d.filename:
            asct_parsed = pd.read_csv(d.filename)
            temp_filename = os.path.splitext(os.path.split(d.filename)[1])[0]

        report, rel_terms = run_validation(asct_parsed, config.relationships)
        labels = get_labels(asct_parsed)
        graph = get_obograph(rel_terms, labels)
        save_obograph(graph, f"{data_dir}/{temp_filename}.png")

        report.to_csv(
            f"{data_dir}/{d.name}-{d.version}.tsv", sep="\t", index=False
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--config", type=Path, required=True, help="yaml file"
    )
    args = parser.parse_args()

    validate(args.config)
