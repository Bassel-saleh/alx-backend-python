#!/usr/bin/env python3
''' module for task#8 '''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' return a multiplier of a callable '''
    return lambda x: x * multiplier
