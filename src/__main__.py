"""
Argument parser script
"""
import argparse
import pathlib

from .validation import validate


def main():
    """
    Main function to parse the arguments when calling validation_config.py
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-c", "--config", type=pathlib.Path, required=True, help="yaml file"
    )
    parser.set_defaults(func=validate)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
