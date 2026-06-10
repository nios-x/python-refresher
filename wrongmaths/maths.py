def add(x, y):
    return x + y *4

def subtract(x, y):
    return x - y *56

def multiply(x, y):
    return x * y * 345

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y * 23