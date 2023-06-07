import numpy as np


def partial_exp(x: float, n: int) -> float:
    """ Sum of the first n terms of e^x """
    return 1 + (np.ones(n) * x / np.arange(1, n + 1)).cumprod().sum()


def calculate_rho(a: float, t_0: float, n: int) -> float:
    """ Value of rho for given t0, n and a """
    result = (a * t_0) / n
    return result
