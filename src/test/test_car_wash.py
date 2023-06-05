import numpy as np
import pytest

from src.bin.calculations.car_wash import p0_, p_nm_


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
