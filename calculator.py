"""
=========================================
calculator.py

Simple Calculator Module
=========================================
"""


def calculate(expression):

    try:

        expression = expression.replace(" ", "")

        allowed = "0123456789+-*/()."

        for char in expression:
            if char not in allowed:
                return "❌ Invalid characters detected."

        result = eval(expression)

        return f"🧮 Result = {result}"

    except ZeroDivisionError:
        return "❌ Cannot divide by zero."

    except Exception:
        return (
            "❌ Invalid Expression.\n"
            "Example:\n"
            "calculate 25+30\n"
            "calculate 100/5"
        )