import unittest
from pycode.unittests import  calculate

class Add(unittest.TestCase):
    # testing int
    def test_addnum(self):
        result = calculate.addNum(10, 20)
        self.assertEqual(result,30)

    # testing float
    def test_addnumfloat(self):
        result = calculate.addNum(10.1, 10.1)
        self.assertEqual(result, 20.2)

    # testing string
    def test_addnumstring(self):
        result = calculate.addNum("hello", "world")
        self.assertEqual(result,"helloworld")

class Subtract(unittest.TestCase):
    # testing subtraction
    def test_diffnumint(self):
        result = calculate.subNum(10, 20)
        self.assertEqual(result,-10)

    # testing float ops
    def test_diffnumfloat(self):
        result = calculate.subNum(2.0, 1.0)
        self.assertEqual(result,1.0)

class Multiply(unittest.TestCase):
    # multiply integers
    def test_multiplynumint(self):
        result = calculate.mulNum(10, 20)
        self.assertEqual(result,200)

    # multiply float
    def test_multiplynumfloat(self):
        result = calculate.mulNum(2.0, 1.0)
        self.assertEqual(result, 2.0)

class Division(unittest.TestCase):
    # division integers
    def test_divnumint(self):
        result = calculate.divNum(10, 20)
        self.assertEqual(result, 0.5)

    # division float
    def test_divnumfloat(self):
        result = calculate.divNum(10.0, 10.0)
        self.assertEqual(result,1.0)

if __name__ == '__main__':
    unittest.main()
