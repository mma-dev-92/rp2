import logging

from config import Parameters
import numpy as np


class P0:
    def __init__(self, n: int, rho: float) -> None:
        self._m = 0
        self._rho = rho
        self._sum_value = self._sum(n, rho)
        self._const = self._constant_term(n, rho)
        self._precomputed = {0: self._const}

    @staticmethod
    def _sum(n: int, rho: float):
        """
        p0 formula sum (from 0 to n)
        :param n: number of car slots in the car wash
        :param rho: precomputed value of rho
        :return: value of the sum_{k=0}^n (n*rho)^k/k! expression
        """
        arr = np.ones(n) * n*rho / np.arange(1, n + 1)
        return 1 + arr.cumprod().sum()

    @staticmethod
    def _constant_term(n: int, rho: float) -> float:
        """
        p0 formula constant term (not depending on m)
        :param n: number of car slots in the car wash
        :param rho: precomputed value of rho
        :return: value of the (rho*(n*rho)^n) / (n!(1-rho)) expression
        """
        return rho * (n*rho) ** n / np.math.factorial(n) / (1 - rho)

    def __getitem__(self, _m: int) -> float:
        """
        Value of p0 for given m
        :param _m: value of m
        :return: p0[m]
        """
        while self._m < _m:
            next_value = self._precomputed[self._m] * self._rho
            validate_overflow(next_value)
            self._precomputed[self._m + 1] = next_value
            self._m += 1

        result = 1 / (self._sum_value + self._const - self._precomputed[_m])
        validate_overflow(result)

        return result


class Pnm:
    def __init__(self, n: int, rho: float, p0: P0) -> None:
        self._m = 0
        self._rho = rho
        self._p0 = p0
        self._precomputed = {0: self._constant_term(n, rho)}

    @staticmethod
    def _constant_term(n: int, rho: float) -> float:
        """
        p_{n+k} formula constant term
        :param n: number of car slots in the car wash
        :param rho: precomputed value of rho
        :return: value of the (n*rho)^n / n! expression
        """
        return (n * rho) ** n / np.math.factorial(n)

    def __getitem__(self, _m: int):
        """
        Value of p_{n+m} for given m
        :param _m: value of m
        :return: p_{n+k}[m]
        """
        while self._m < _m:
            next_value = self._precomputed[self._m] * self._rho
            validate_overflow(next_value)
            self._precomputed[self._m + 1] = next_value
            self._m += 1

        result = self._precomputed[_m] * self._rho * self._p0[_m]
        validate_overflow(result)
        return result


def calculate_rho(params: Parameters) -> float:

    result = (params.a * params.t_0) / params.n
    if result >= 1.0:
        raise ValueError(
            f"rho cannot be greater or equal to 1.0, verify input parameters!")
    if result < 0.9:
        logging.warning(
            f"rho is smaller than 0.9, are you sure, that the input parameters are correct? [this is just warning, "
            f"computations will go on]"
        )
    return (params.a * params.t_0) / params.n


def calculate_m(params: Parameters, p0_gen: P0, p_nm_gen: Pnm) -> int:
    n, p, t_0 = params.n, params.p, params.t_0
    m, p0, p_nm = 0, p0_gen[0], p_nm_gen[0]
    while 1 - p_nm < p:
        p_nm = p_nm_gen[m + 1]
        m += 1

    if m == 0:
        logging.warning(
            f"computed value m={m}, please verify input parameters (probably 'p' value compared to 'n' value is is to "
            f"small) [this is just warning, program will not crush, but results might be strange]")

    return m


def calculate_w1(params: Parameters, m: int, p0_gen: P0, p_nm_gen: Pnm) -> float:
    n, t_0 = params.n, params.t_0
    factor = t_0 / (1 - p0_gen[m]) / n
    sum_value, k = 0, n
    while k <= n + m - 1:
        sum_value += p_nm_gen[k - n] * k
        k += 1

    return factor * sum_value


def calculate(params: Parameters):
    n, rho = params.n, calculate_rho(params)
    p0_gen = P0(n, rho)
    p_nm_gen = Pnm(n, rho, p0_gen)

    m = calculate_m(params, p0_gen, p_nm_gen)
    w1 = calculate_w1(params, m, p0_gen, p_nm_gen)

    return m, w1


def validate_overflow(arr: float) -> None:
    if np.isnan(arr):
        raise OverflowError(f"computation crushed: number of bits exceeded")

