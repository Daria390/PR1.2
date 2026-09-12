import math

def calculate_expression(x):
    if x + 3 < 0:
        return "Error: Expression under square root (x + 3) must be non-negative."
    
    denominator = math.sqrt(x + 3)
    if denominator == 0:
        return "Error: Division by zero (denominator is 0)."
    
    y = (math.sin(x) + x**2) / denominator
    return y