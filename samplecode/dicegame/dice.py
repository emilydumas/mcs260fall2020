"""Module that simulates rolling dice"""

import random

def roll(sides):
    """Roll a single die with `sides` sides"""
    return random.randint(1,sides)

def roll_many(sides,times):
    """Roll a `sides`-sided die `times` times, return a
    list of rolls.
    """
    return [ roll(sides) for i in range(times) ]

def roll_sum(sides,times):
    """Roll a `sides`-sided die `times` times, return the
    sum of the rolls.
    """
    accum = 0
    for i in range(times):
        accum = accum + roll(sides)
    return accum
