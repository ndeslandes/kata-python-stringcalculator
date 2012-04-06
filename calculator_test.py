import unittest
from calculator import Calculator

class CalculatorTest(unittest.TestCase):
    
    def setUp(self):
        self.calculator = Calculator()
    
    def test_add_withEmptyString_shouldReturnZero(self):
        self.assertEquals(self.calculator.add(''), 0)

    def test_add_withOneNumber_shouldReturnThisNumber(self):
        self.assertEquals(self.calculator.add('1'), 1)
        self.assertEquals(self.calculator.add('0'), 0)

    def test_add_withMultipleNumber_separatedByComma_shouldReturnTheSum(self):
        self.assertEquals(self.calculator.add('1,2'), 3)
        self.assertEquals(self.calculator.add('10,2'), 12)
        
    def test_add_withMultipleNumber_separatedByNewLine_shouldReturnTheSum(self):
        self.assertEquals(self.calculator.add('1\n2'), 3)
        self.assertEquals(self.calculator.add('10\n2'), 12)
        
    def test_add_withMultipleNumber_startingWithDoubleSlash_separatedByDescribeDelimiters_shouldReturnTheSum(self):
        self.assertEquals(self.calculator.add('//?\n1?2'), 3)
        self.assertEquals(self.calculator.add('//+\n10+2'), 12)
        self.assertEquals(self.calculator.add('//abc\n1abc2'), 3)
        
    def test_add_withMultipleNumber_startingWithDoubleSlash_withMixedDelimiters_shouldReturnTheSum(self):
        self.assertEquals(self.calculator.add('//*\n1*10\n4'), 15)
        
    def test_add_withOneNegativeNumber_shouldRaiseValueError(self):
        self.assertRaises(ValueError, self.calculator.add, '-1')
        
    def test_add_withOneNegative_withinTwoNumber_shouldRaiseValueError(self):
        self.assertRaises(ValueError, self.calculator.add, '1,-1')

    def test_add_withMultipleNumber_startingWithDoubleSlash_separatedByMinusDelimiters_shouldReturnTheSum(self):
        self.assertEquals(self.calculator.add('//-\n1-2'), 3)

if __name__ == '__main__':
    unittest.main()
