"""Testing the Calculator"""
# From specifies the namespace
from calculator import Calculator


def test_calculator_add_method():
    """Testing the Calculator add"""
    calculator = Calculator()
    # this is show using the calculator object add method
    assert calculator.add(1, 1) == 2

def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    calculator = Calculator()
    assert calculator.subtract(1, 1) == 0

def test_calculator_multiply_method():
    """Testing the Calculator multiply"""
    calculator = Calculator()
    assert calculator.multiply(1, 1) == 1

def test_calculator_divide_method():
    """Testing the Calculator divide"""
    calculator = Calculator()
    assert calculator.divide(1, 1) == 1