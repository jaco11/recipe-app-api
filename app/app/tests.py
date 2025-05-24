"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Tests for calc module."""

    def test_add_numbers(self):
        """Test Adding Numbers Together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test Subtracting Numbers"""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)