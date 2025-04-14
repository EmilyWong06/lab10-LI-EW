import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(2,2),4)
        self.assertEqual(mul(0,2),0)
        self.assertEqual(mul(1,1000),1000)
        self.assertNotEqual(mul(3,2),4)
        self.assertNotEqual(mul(0,2),2)
        self.assertNotEqual(mul(10,2),21)

    def test_divide(self):
        self.assertEqual(div(2,2),1)
        self.assertEqual(div(100,10),10)
        self.assertEqual(div(0,2),0)
        self.assertNotEqual(div(4,2),3)
        self.assertNotEqual(div(10,3),2)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    def test_log_invalid_argument(self):
        self.assertRaises(ValueError, logarithm(0, 5))
        self.assertRaises(ValueError, logarithm(1, 5))
        self.assertRaises(ValueError, logarithm(10, -4))
        self.assertRaises(ValueError, logarithm(10, 0))

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    def test_hypotenuse(self):
        self.assertEqual(div(3,4),5)
        self.assertEqual(div(5,12),13)
        self.assertEqual(div(8,15),17)


    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

    def test_sqrt(self):
        self.assertRaises(ValueError, square_root(-10))
        self.assertRaises(ValueError, square_root(-1))
        self.assertRaises(ValueError, square_root(-31))
        self.assertRaises(ValueError, square_root(-90))


# Do not touch this
if __name__ == "__main__":
    unittest.main()