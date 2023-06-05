import numpy as np

from src.bin.calculations.utils import calculate_rho, partial_exp
from src.bin.preprocessing import CheckoutQueueParams


def _free_p0_therm(rho: float, n: int) -> float:
    """ Term in p0 formula, that is outside the sum over k """
    return rho * (n*rho) ** n / np.math.factorial(n) / (1 - rho)


def p0_(rho: float, n: int) -> float:
    """ For given rho and n calculate p0 """
    return 1 / (partial_exp(rho * n, n) + _free_p0_therm(rho, n))


def P_(rho: float, n: int, L: int) -> float:
    """ For given rho, n, L calculate P """
    return p0_(rho, n) * (partial_exp(rho * n, n) + _free_p0_therm(rho, n) * (1 - rho ** L))


def calculate_n(a: float, t_0: float, Q: float, L: int) -> int:
    """ Calculate minimal value of n, for which P >= Q """
    n = int(a * t_0) + 1
    rho = calculate_rho(a, t_0, n)
    P_value = P_(rho, n, L)
    while P_value < Q:
        P_value = P_(rho, n + 1, L)
        n = n + 1
    return n


def checkout_queue_calculations(params: CheckoutQueueParams):
    return calculate_n(a=params.a, t_0=params.t_0, Q=params.Q, L=params.L)
