def simple_calculator(num1, num2, operator):
    """
    Performs a simple calculation using two numbers and an operator.
    Supported operators: +, -, *, /
    """
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                raise ValueError("Cannot divide by zero.")
            result = num1 / num2
        else:
            raise ValueError("Invalid operator. Use one of: +, -, *, /")

        return f"Result: {num1} {operator} {num2} = {result}"

    except ValueError as e:
        raise ValueError(f"Error: {str(e)}")
