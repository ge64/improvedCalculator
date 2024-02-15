import pytest
from decimal import Decimal
from calculator.calculator import Calculator


@pytest.fixture
def calculator():
    """Fixture to create a Calculator instance for testing."""
    return Calculator()


def test_add(calculator):
    assert calculator.perform_operation("add", Decimal('1'), Decimal('1')) == Decimal('2')


def test_subtract(calculator):
    assert calculator.perform_operation("subtract", Decimal('5'), Decimal('3')) == Decimal('2')


def test_multiply(calculator):
    assert calculator.perform_operation("multiply", Decimal('2'), Decimal('3')) == Decimal('6')


def test_divide(calculator):
    assert calculator.perform_operation("divide", Decimal('10'), Decimal('2')) == Decimal('5')


def test_divide_by_zero(calculator):
    with pytest.raises(ValueError) as e:
        calculator.perform_operation("divide", Decimal('10'), Decimal('0'))
    assert str(e.value) == "Cannot divide by zero"


def test_get_last_calculation(calculator):
    calculator.perform_operation("add", Decimal('1'), Decimal('1'))
    operation, result = calculator.get_last_calculation()
    assert operation == "add" and result == Decimal('2')


def test_history(calculator):
    calculator.perform_operation("multiply", Decimal('2'), Decimal('3'))
    last_op, last_result = calculator.get_last_calculation()
    assert last_op == "multiply" and last_result == Decimal('6')
