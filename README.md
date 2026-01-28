# Calculator Application

A simple command-line calculator that supports basic arithmetic operations.

## Features

- **Addition** (+): Add two numbers
- **Subtraction** (-): Subtract the second number from the first
- **Multiplication** (*): Multiply two numbers
- **Division** (/): Divide the first number by the second

## Requirements

- Python 3.6 or higher

## Usage

### Running the Calculator

Run the calculator from the command line:

```bash
python calculator.py
```

Or make it executable and run directly:

```bash
chmod +x calculator.py
./calculator.py
```

### Interactive Mode

Once started, the calculator will prompt you for:

1. **First number**: Enter any valid number (integers or decimals)
2. **Operation**: Enter one of the supported operations (+, -, *, /)
3. **Second number**: Enter another valid number

The result will be displayed, and you can continue with more calculations.

### Example Session

```
========================================
       Simple Calculator
========================================
Supported operations: +, -, *, /
Type 'quit' or 'exit' to exit
========================================

Enter first number (or 'quit' to exit): 10
Enter operation (+, -, *, /): +
Enter second number: 5

Result: 10.0 + 5.0 = 15

Enter first number (or 'quit' to exit): 20
Enter operation (+, -, *, /): /
Enter second number: 4

Result: 20.0 / 4.0 = 5

Enter first number (or 'quit' to exit): quit
Thank you for using the calculator. Goodbye!
```

### Exiting the Calculator

To exit the calculator, you can:
- Type `quit`, `exit`, or `q` when prompted for the first number
- Press `Ctrl+C` to interrupt the program

## Error Handling

The calculator handles the following error cases:

- **Invalid numbers**: If you enter a non-numeric value, an error message will be displayed
- **Invalid operations**: If you enter an unsupported operation, an error message will be displayed
- **Division by zero**: If you attempt to divide by zero, an error message will be displayed

Example error handling:

```
Enter first number (or 'quit' to exit): abc

Error: Invalid number: 'abc'

Enter first number (or 'quit' to exit): 10
Enter operation (+, -, *, /): %

Error: Invalid operation: '%'. Valid operations are: +, -, *, /

Enter first number (or 'quit' to exit): 10
Enter operation (+, -, *, /): /
Enter second number: 0

Error: Cannot divide by zero
```
