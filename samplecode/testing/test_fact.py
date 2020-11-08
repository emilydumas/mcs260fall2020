"""Tests for the module fact"""

import fact

def test_initial_0():
    """Test 0!"""
    assert fact.fact(0) == 1

def test_initial_1():
    """Test 1!"""
    assert fact.fact(1) == 1

def test_recursion():
    """Test factorials for larger integer values
    that will therefore use the recursive call in
    fact.fact().  We compare the results to a 
    precomputed list.
    """
    expected_input_output = [ (4,24), (5,120), (6,720) ]

    for x,yexpected in expected_input_output:
        yactual = fact.fact(x)
        print("fact.fact({})={}, and the expected value was {}".format(
            x,
            yactual,
            yexpected
        ))
        assert yactual == yexpected

