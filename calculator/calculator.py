from decimal import Decimal
from calculator.operations import add, subtract, multiply, divide


class Calculator:
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
            return result
        except KeyError:
            raise ValueError(f"Operation '{operation}' is not supported.")
