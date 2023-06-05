import numpy as np
import pytest

from src.bin.calculations.checkout_queue import p0_, P_


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
