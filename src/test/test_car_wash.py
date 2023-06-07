import numpy as np
import pytest

from src.bin.calculations.car_wash import p0_, p_nm_, calculate_m, calculate_w1


@pytest.mark.parametrize(
    ("rho", "n", "m", "expected_result"),
    [
        (0.5, 3, 0, 1 / (1 + 1.5 + 1.5 ** 2 / 2 + 1.5 ** 3 / 6)),
        (0.5, 3, 1, 1 / (1 + 1.5 + 1.5 ** 2 / 2 + 1.5 ** 3 / 6 + 1.5 ** 3 / 12)),
        (2/3, 3, 2, 1 / (5 + 4 / 3 + 2 ** 4 * (1 - (2 / 3) ** 2) / 6))
    ]
)
def test_p0_(rho: float, n: int, m: int, expected_result: float) -> None:
    assert np.isclose(p0_(rho, n, m), expected_result)


@pytest.mark.parametrize(
    ("rho", "n", "m", "expected_result"),
    [
        (0.5, 3, 0, 3 ** 3 * 0.5 ** 3 / (1 + 1.5 + 1.5 ** 2 / 2 + 1.5 ** 3 / 6) / 6),
        (2 / 3, 3, 2, 3 ** 3 * (2 / 3) ** 5 / (5 + 4 / 3 + 2 ** 4 * (1 - (2 / 3) ** 2) / 6) / 6)
    ]
)
def test_p_nm_(rho: float, n: int, m: int, expected_result: float) -> None:
    assert np.isclose(p_nm_(rho, n, m), expected_result)


@pytest.mark.parametrize(
    ("a", "t_0", "P", "n", "expected_value"),
    [
        (4, 0.7, 0.9, 3, 5),
        (5, 0.5, 0.8, 4, 0),
        (7, 0.4, 0.75, 3, 1),
        (5, 0.3, 0.85, 2, 2)
    ]
)
def test_calculate_m(a: float, t_0: float, P: float, n: int, expected_value: float) -> None:
    assert calculate_m(a, t_0, n, P) == expected_value


@pytest.mark.parametrize(
    ("a", "t_0", "n", "m", "expected_result"),
    [
        (4, 0.7, 3, 5, 0.765),
        (5, 0.5, 4, 0, 0),
        (7, 0.4, 3, 1, 0.129),
        (5, 0.3, 2, 2, 0.160)
    ]
)
def test_calculate_w1(a: float, t_0: float, n: int, m: int, expected_result: float) -> None:
    assert np.abs(calculate_w1(a, t_0, n, m) - expected_result) < 1e-3
