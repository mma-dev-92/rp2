import sys

from calculations import calculate
from config import load_ini_file
from parser import get_path_from_cli

if __name__ == '__main__':
    config_ini_path = get_path_from_cli(sys.argv)
    params = load_ini_file(config_ini_path)
    m, w1 = calculate(params)

    print(f" * m = {m}\n * w1 = {w1}")
