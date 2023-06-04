from configparser import ConfigParser
from dataclasses import dataclass
from pathlib import Path


class ValidationError(Exception):
    pass


_ini_file_section = "parameters"
_param_names = {'n', 't_0', 'a', 'P'}


@dataclass
class Parameters:
    n: int
    t_0: float
    a: float
    p: float


def load_ini_file(file_path: Path) -> Parameters:
    cfg = ConfigParser()
    cfg.read(file_path)
    validate_config_file(cfg)

    return Parameters(
        n=cfg[_ini_file_section].getint('n'),
        t_0=cfg[_ini_file_section].getfloat('t_0'),
        a=cfg[_ini_file_section].getfloat('a'),
        p=cfg[_ini_file_section].getfloat('P')
    )


def validate_config_file(_cfg: ConfigParser) -> None:

    assert _cfg.sections() == [_ini_file_section], \
        f"given config file has invalid sections, should have only one section: [{_ini_file_section}]"

    assert set(_cfg[_ini_file_section].keys()) == {'a', 'p', 't_0', 'n'}, \
        f"given config file has invalid parameters, it should have only {list(_param_names)} parameters"
