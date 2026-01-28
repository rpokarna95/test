#!/usr/bin/env python3
"""
A simple calculator application supporting basic arithmetic operations.
"""


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide the first number by the second.
    
    Raises:
        ZeroDivisionError: If the second number is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


OPERATIONS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def get_number(prompt: str) -> float:
    """Get a valid number from user input.
    
    Args:
        prompt: The prompt to display to the user.
        
    Returns:
        The number entered by the user.
        
    Raises:
        ValueError: If the input is not a valid number.
    """
    user_input = input(prompt).strip()
    try:
        return float(user_input)
    except ValueError:
        raise ValueError(f"Invalid number: '{user_input}'")


def get_operation() -> str:
    """Get a valid operation from user input.
    
    Returns:
        The operation symbol (+, -, *, /).
        
    Raises:
        ValueError: If the input is not a valid operation.
    """
    valid_ops = ', '.join(OPERATIONS.keys())
    user_input = input(f"Enter operation ({valid_ops}): ").strip()
    if user_input not in OPERATIONS:
        raise ValueError(f"Invalid operation: '{user_input}'. Valid operations are: {valid_ops}")
    return user_input


def calculate(num1: float, operation: str, num2: float) -> float:
    """Perform the calculation.
    
    Args:
        num1: The first operand.
        operation: The operation to perform (+, -, *, /).
        num2: The second operand.
        
    Returns:
        The result of the calculation.
    """
    operation_func = OPERATIONS[operation]
    return operation_func(num1, num2)


def format_result(result: float) -> str:
    """Format the result for display.
    
    Args:
        result: The calculation result.
        
    Returns:
        A formatted string representation of the result.
    """
    if result == int(result):
        return str(int(result))
    return str(result)


def run_calculator():
    """Run the interactive calculator."""
    print("=" * 40)
    print("       Simple Calculator")
    print("=" * 40)
    print("Supported operations: +, -, *, /")
    print("Type 'quit' or 'exit' to exit")
    print("=" * 40)
    
    while True:
        print()
        try:
            first_input = input("Enter first number (or 'quit' to exit): ").strip().lower()
            if first_input in ('quit', 'exit', 'q'):
                print("Thank you for using the calculator. Goodbye!")
                break
            
            try:
                num1 = float(first_input)
            except ValueError:
                raise ValueError(f"Invalid number: '{first_input}'")
            
            operation = get_operation()
            num2 = get_number("Enter second number: ")
            
            result = calculate(num1, operation, num2)
            formatted_result = format_result(result)
            print(f"\nResult: {num1} {operation} {num2} = {formatted_result}")
            
        except ZeroDivisionError as e:
            print(f"\nError: {e}")
        except ValueError as e:
            print(f"\nError: {e}")
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted. Goodbye!")
            break
        except EOFError:
            print("\n\nNo input received. Goodbye!")
            break


if __name__ == "__main__":
    run_calculator()
