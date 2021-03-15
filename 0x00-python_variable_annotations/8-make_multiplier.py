#!/usr/bin/env python3
"""
returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function that multiplies a float by multiplier.
    """
    def f(m: float):
        return multiplier * m
    return f
