from decimal import Decimal
from typing import Tuple, List
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    _history: List[Tuple[str, Decimal]] = []

    # Mapping of operations to their corresponding functions
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    @staticmethod
    def perform_operation(operation: str, a: Decimal, b: Decimal) -> Decimal:
        """Performs the given operation on two Decimal numbers."""
        try:
            result = Calculator.operations[operation](a, b)
            Calculator._add_to_history(operation, result)
            return result
        except KeyError:
            raise ValueError(f"Operation '{operation}' is not supported.")

    @classmethod
    def _add_to_history(cls, operation: str, result: Decimal) -> None:
        """Adds an operation and its result to the history."""
        cls._history.append((operation, result))

    @classmethod
    def get_last_calculation(cls) -> Tuple[str, Decimal]:
        """Retrieves the last calculation from the history."""
        try:
            return cls._history[-1]
        except IndexError:
            raise ValueError("No calculations in history.")
