import numpy as np

from src.bin.calculations.utils import calculate_rho, partial_exp
from src.bin.preprocessing import CarWashParams


def _free_p0_therm(rho: float, n: int, m: int) -> float:
    """ Term in p0 formula, that is outside the sum over k """
    return (1 - rho ** m) * rho * (n*rho) ** n / np.math.factorial(n) / (1 - rho)


def p0_(rho: float, n: int, m: int) -> float:
    """ For given rho, n and m calculate p0 """
    return 1 / (partial_exp(rho * n, n) + _free_p0_therm(rho, n, m))


def p_nm_(rho: float, n: int, m: int) -> float:
    """ For given rho, n and m calculate p_{n+m} """
    return p0_(rho, n, m) * ((n * rho) ** n) * (rho ** m) / np.math.factorial(n)


def calculate_m(a: float, t_0: float, n: int, P: float) -> int:
    """ For given t_0, a, n and P calculate minimal value of m """
    m = 0
    rho = calculate_rho(a, t_0, n)
    p_nm_value = p_nm_(rho, n, m)
    while 1 - p_nm_value < P:
        p_nm_value = p_nm_(rho, n, m + 1)
        m = m + 1

    return m


def calculate_w1(a: float, t_0: float, n: int, m: int) -> float:
    """ minimal value of m calculate expected await time w1 for given t_0, n, m and a """
    rho = calculate_rho(a, t_0, n)
    p0_value = p0_(rho, n, m)
    factor = t_0 * p0_value * n ** n / np.math.factorial(n) / (1 - p_nm_(rho, n, m)) / n
    return factor * sum([(rho ** k) * k for k in range(n, n + m)])


def car_wash_calculations(params: CarWashParams):
    P, a, t_0, n = params.P, params.a, params.t_0, params.n
    m = calculate_m(a=a, t_0=t_0, n=n, P=P)
    w1 = calculate_w1(a=a, t_0=t_0, n=n, m=m)

    return m, w1
