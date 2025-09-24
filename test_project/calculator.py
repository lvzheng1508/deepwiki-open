#!/usr/bin/env python3
"""
Simple Calculator Application

A basic calculator that performs arithmetic operations with error handling.
"""

class Calculator:
    """A simple calculator class that performs basic arithmetic operations."""
    
    def __init__(self):
        """Initialize the calculator."""
        self.history = []
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract second number from first number.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Difference of a and b
        """
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
        """
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """Divide first number by second number.
        
        Args:
            a: Dividend
            b: Divisor
            
        Returns:
            Quotient of a and b
            
        Raises:
            ValueError: If divisor is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self) -> list:
        """Get calculation history.
        
        Returns:
            List of calculation history
        """
        return self.history.copy()
    
    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()


def main():
    """Main function to demonstrate calculator usage."""
    calc = Calculator()
    
    print("Simple Calculator")
    print("================")
    
    try:
        # Test basic operations
        print(f"5 + 3 = {calc.add(5, 3)}")
        print(f"10 - 4 = {calc.subtract(10, 4)}")
        print(f"6 * 7 = {calc.multiply(6, 7)}")
        print(f"15 / 3 = {calc.divide(15, 3)}")
        
        # Test error handling
        try:
            calc.divide(10, 0)
        except ValueError as e:
            print(f"Error: {e}")
        
        # Show history
        print("\nCalculation History:")
        for entry in calc.get_history():
            print(f"  {entry}")
            
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
