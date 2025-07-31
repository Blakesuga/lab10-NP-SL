#https://github.com/Blakesuga/lab10-NP-SL
# Partner 1: Natania Philippe
# Partner 2: Seth Lea

import unittest
from calculator import *



class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    def test_add(self):
        self.assertEqual(add(3, 9), 12)
        self.assertEqual(add(5,1),6)
        self.assertEqual(add(4,3), 7)

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################
    def test_subtract(self):
        self.assertEqual(sub(10, 9), 1)
        self.assertEqual(sub(8, 2), 6)
        self.assertEqual(sub(6, 3),3)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 9), 27)
        self.assertEqual(mul(6, 6), 36)
        self.assertEqual(mul(4, 24), 108)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(3, 9), 3)
        self.assertAlmostEqual(div(6, 7), 1.16666667)
        self.assertRaises(div(0, 7), ZeroDivisionError)

    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)


    # def test_logarithm(self): # 3 assertions
    #     fill in code
    def test_logarithm(self):
        self.assertEqual(log(100, 10), 2)
        self.assertEqual(log(8, 2), 3)
        self.assertEqual(log(1, 10), 0)

    # def test_log_invalid_base(self): # 1 assertion
    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(10, 1)



    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(4, 5), 41)
        self.assertEqual(hypotenuse(2, 3), 13)
        self.assertEqual(hypotenuse(7, 4), 65)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
           square_root(-1)

        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(1), 1)




# Do not touch this
if __name__ == "__main__":
    unittest.main()