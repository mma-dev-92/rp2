import numpy as np
import pytest

from src.bin.calculations.utils import partial_exp, calculate_rho


@pytest.mark.parametrize(
    ("x", "n", "expected_result"),
    [
        (3, 0, 1),
        (2.55, 0, 1),
        (-1.2, 0, 1),
        (1, 3, 2.5 + 1/6),
        (0.5, 4, 1.5 + 0.5 ** 2 / 2 + 0.5 ** 3 / 6 + 0.5 ** 4 / 24)
    ]
)
def test_partial_exp(x: float, n: int, expected_result: float) -> None:
    assert np.isclose(partial_exp(x, n), expected_result)


@pytest.mark.parametrize(
    ("a", "t_0", "n", "expected_result"),
    [
        (1, 1, 3.0, 1/3), (1, 2, 3, 2 / 3), (0, 1, 1, 0), (1, 0, 1, 0)
    ]
)
def test_calculate_rho(a: float, t_0: float, n: int, expected_result: float) -> None:
    assert np.isclose(calculate_rho(a, t_0, n), expected_result)
