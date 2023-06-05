from configparser import ConfigParser
from dataclasses import dataclass
from pathlib import Path


class ValidationError(Exception):
    pass


_car_wash_section = "car_wash"
_checkout_queue_section = "checkout_queue"

_init_file_structure = {
    "car_wash": {'n', 't_0', 'a', 'P'},
    "checkout_queue": {'a', 't_0', 'Q', 'L'}
}


def load_ini_file(file_path: Path) -> ConfigParser:
    cfg = ConfigParser()
    cfg.optionxform = str
    cfg.read(file_path)
    validate_config_file(cfg)
    return cfg


def validate_config_file(_cfg: ConfigParser) -> None:
    expected_sections = set(_cfg.sections())
    given_sections = set(_init_file_structure)
    assert expected_sections == given_sections, \
        f"given config file has invalid sections: {given_sections}, but should have: {expected_sections}"

    for section in given_sections:
        given_parameters = set(_cfg[section])
        expected_parameters = _init_file_structure[section]
        assert given_parameters == expected_parameters, \
            f"section {section} has wrong parameters: {given_parameters}, but should have {expected_parameters}"


@dataclass
class CarWashParams:
    n: int
    t_0: float
    a: float
    P: float

    @classmethod
    def create(cls, _cfg: ConfigParser) -> 'CarWashParams':
        data = _cfg[_car_wash_section]
        return cls(
            n=data.getint('n'),
            t_0=data.getfloat('t_0'),
            a=data.getfloat('a'),
            P=data.getfloat('P')
        )


@dataclass
class CheckoutQueueParams:
    a: float
    t_0: float
    Q: float
    L: int

    @classmethod
    def create(cls, _cfg: ConfigParser) -> 'CheckoutQueueParams':
        data = _cfg[_checkout_queue_section]
        return cls(
            a=data.getfloat('a'),
            t_0=data.getfloat('t_0'),
            Q=data.getfloat('Q'),
            L=data.getint('L')
        )


@dataclass
class Parameters:
    car_wash: CarWashParams
    checkout_queue: CheckoutQueueParams

    @classmethod
    def create(cls, _cfg: ConfigParser) -> 'Parameters':
        return cls(
            car_wash=CarWashParams.create(_cfg),
            checkout_queue=CheckoutQueueParams.create(_cfg)
        )


def load_data(file_path: Path) -> Parameters:
    return Parameters.create(load_ini_file(file_path))
