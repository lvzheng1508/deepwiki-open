#!/usr/bin/env python3
"""
Unit tests for the Calculator class.
"""

import unittest
import sys
import os

# Add parent directory to path to import calculator
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()
    
    def test_addition(self):
        """Test addition operation."""
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
    
    def test_subtraction(self):
        """Test subtraction operation."""
        result = self.calc.subtract(10, 4)
        self.assertEqual(result, 6)
    
    def test_multiplication(self):
        """Test multiplication operation."""
        result = self.calc.multiply(3, 4)
        self.assertEqual(result, 12)
    
    def test_division(self):
        """Test division operation."""
        result = self.calc.divide(15, 3)
        self.assertEqual(result, 5)
    
    def test_division_by_zero(self):
        """Test division by zero error handling."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    def test_history(self):
        """Test calculation history."""
        self.calc.add(1, 2)
        self.calc.subtract(5, 3)
        
        history = self.calc.get_history()
        self.assertEqual(len(history), 2)
        self.assertIn("1 + 2 = 3", history)
        self.assertIn("5 - 3 = 2", history)
    
    def test_clear_history(self):
        """Test clearing calculation history."""
        self.calc.add(1, 2)
        self.calc.clear_history()
        
        history = self.calc.get_history()
        self.assertEqual(len(history), 0)


if __name__ == "__main__":
    unittest.main()
