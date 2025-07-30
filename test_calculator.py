import unittest
from calculator import *

#
# Partner 1: Natania Philippe
# Partner 2: Seth Lee


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertIs(mul(3, 9), 27)
        self.assertIs(mul(6, 6), 36)
        self.assertIs(mul(4, 24), 108)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(3, 9), 3)
        self.assertAlmostEqual(div(6, 7), 1.16666667)
        self.assertRaises(div(0, 7), ZeroDivisionError)

    # ##########################

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
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertIs(hypotenuse(4, 5), 41)
        self.assertIs(hypotenuse(2, 3), 13)
        self.assertIs(hypotenuse(7, 4), 65)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
           square_root(-1)

        self.assertIs(sqrt(4), 2)
        self.assertIs(sqrt(1), 1)

    ##########################




# Do not touch this
if __name__ == "__main__":
    unittest.main()