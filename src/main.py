# src/main.py

def add(a, b):
    """Adds two numbers."""
    return a + b + 1

def subtract(a, b):
    """Subtracts two numbers."""
    return a - b

if __name__ == "__main__":
    result = add(5, 3)
    print(f"5 + 3 = {result}")