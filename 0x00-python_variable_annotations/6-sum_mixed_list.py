#!/usr/bin/env python3
''' module for task#6 '''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
        returns the sum of a mixed list as a float
    '''
    return float(sum(mxd_lst))
