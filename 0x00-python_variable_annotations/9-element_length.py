#!/usr/bin/env python3
''' module for task#9 '''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
        Computes the length of each sequence in the provided iterable.
    '''
    return [(i, len(i)) for i in lst]
