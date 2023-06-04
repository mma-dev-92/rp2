from pathlib import Path

from calculations import calculate
from config import load_ini_file


if __name__ == '__main__':
    params = load_ini_file(Path('config.ini'))
    m, w1 = calculate(params)

    print(f" * m = {m}\n * w1 = {w1}")
