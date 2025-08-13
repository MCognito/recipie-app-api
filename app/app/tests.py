"""
Sample Tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""
    def test_add(self):
        """Test adding numbers"""
        res = calc.add(10, 5)
        self.assertEqual(res, 15)

    def test_subtract(self):
        """Test subtracting numbers"""
        res = calc.subtract(10, 5)
        self.assertEqual(res, 5)

    def test_multiply(self):
        """Test multiplying numbers"""
        res = calc.multiply(10, 5)
        self.assertEqual(res, 50)

    def test_divide(self):
        """Test dividing numbers"""
        res = calc.divide(10, 5)
        self.assertEqual(res, 2)
