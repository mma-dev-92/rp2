import argparse
from pathlib import Path


def get_path_from_cli() -> Path:
    parser = argparse.ArgumentParser()
    parser.add_argument('config', type=Path)
    args = parser.parse_args()
    return args.config


