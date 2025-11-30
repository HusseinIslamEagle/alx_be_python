from simple_calculator import SimpleCalculator

def test_addition():
    calc = SimpleCalculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0
    assert calc.add(-5, -5) == -10


def test_subtraction():
    calc = SimpleCalculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(3, 5) == -2
    assert calc.subtract(0, 0) == 0
    assert calc.subtract(-5, -5) == 0


def test_multiplication():
    calc = SimpleCalculator()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 50) == 0
    assert calc.multiply(-4, -4) == 16


def test_division():
    calc = SimpleCalculator()
    assert calc.divide(6, 3) == 2
    assert calc.divide(-6, 3) == -2
    assert calc.divide(5, 2) == 2.5  # division float behavior
    assert calc.divide(0, 5) == 0
    assert calc.divide(10, 0) is None  # division by zero case
