# Sample tests

from django.test import SimpleTestCase

from app.calc import Calculator


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        newCalc = Calculator(5, 6)
        res = newCalc.add()
        self.assertEqual(res, 11)
      
    def test_multiply_numbers(self):
        newCalc = Calculator(5, 6)
        res = newCalc.multiply()
        self.assertEqual(res, 30)

