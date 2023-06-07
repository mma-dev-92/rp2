import numpy as np
import pytest

from src.bin.calculations.checkout_queue import p0_, P_, calculate_n


@pytest.mark.parametrize(
    ("rho", "n", "expected_result"),
    [
        (1/3, 2, 1 / (1 + 2/3 + (2/3) ** 2 / 2 + 2 ** 2 * (1/3) ** 3 / 2 / (2 / 3)))
    ]
)
def test_p0_(rho: float, n: int, expected_result: float) -> None:
    assert np.isclose(p0_(rho, n), expected_result)


@pytest.mark.parametrize(
    ("rho", "n", "L", "expected_result"),
    [
        (
            1/3, 2, 1,
            (1 + 2/3 + (2/3) ** 2 / 2 + 2 ** 2 * (1/3) ** 3 / 2)
            / (1 + 2/3 + (2/3) ** 2 / 2 + 2 ** 2 * (1/3) ** 3 / 2 / (2 / 3))
        ),
        (
            1/3, 2, 3,
            (1 + 2/3 + (2/3) ** 2 / 2 + 2 ** 2 * (1/3) ** 3 / 2 / (2 / 3) * (1 - (1 / 3) ** 3))
            / (1 + 2 / 3 + (2 / 3) ** 2 / 2 + 2 ** 2 * (1 / 3) ** 3 / 2 / (2 / 3))

)
    ]
)
def test_P_(rho: float, n: int, L: int, expected_result: float) -> None:
    assert np.isclose(P_(rho, n, L), expected_result)


@pytest.mark.parametrize(
    ("a", "t_0", "L", "Q", "expected_result"),
    [
        (6, 0.6, 4, 0.99, 7),
        (10, 0.15, 5, 0.99, 3),
        (8, 0.3, 7, 0.95, 4),
        (2, 0.8, 6, 0.85, 2)
    ]
)
def test_calculate_n(a: float, t_0: float, L: int, Q: float, expected_result: int) -> None:
    assert calculate_n(a, t_0, Q, L) == expected_result
