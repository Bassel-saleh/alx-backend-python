#!/usr/bin/env python3
''' module for task#7 '''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
        returns a tuple a of string and square of a float
    '''
    return (k, float(v**2))
