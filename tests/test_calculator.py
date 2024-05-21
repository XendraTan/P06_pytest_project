import pytest
from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected
        

    def test_substract(self):
        # arrange
        a = 4000
        b = 1000
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 3000
        assert result == expected
        
    def test_multiply(self):
        # arrange
        a = 4
        b = 10
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 40
        assert result == expected
        

    
    def test_divide(self):
        # arrange
        a = 400
        b = 100
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 4
        assert result == expected
        
