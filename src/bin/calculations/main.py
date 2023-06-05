from src.bin.calculations.car_wash import car_wash_calculations
from src.bin.calculations.checkout_queue import checkout_queue_calculations
from src.bin.parser import get_path_from_cli
from src.bin.preprocessing import load_data


def main():

    config_ini_path = get_path_from_cli()
    params = load_data(config_ini_path)
    m_min, w1 = car_wash_calculations(params.car_wash)
    n_min = checkout_queue_calculations(params.checkout_queue)

    print(f"\n--- car wash simulation results --")
    print(f" * m_min = {m_min}\n * w1 = {w1}")

    print(f"--- checkout queue results ---")
    print(f" * n_min = {n_min}\n")

