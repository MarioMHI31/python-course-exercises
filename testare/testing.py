import unittest
from exercitii_import.math_functions import power


class TestMathFunctions(unittest.TestCase):
    def setUp(self):
        self.num = 5
        self.power = 3

    def test_num_parameter_exists(self):
        self.assertIsNotNone(self.num)

    def test_power_parameter_exists(self):
        self.assertIsNotNone(self.power)

    def test_num_tip(self):
        try:
            self.assertIsInstance(self.num, int)
        except:
            self.assertIsInstance(self.num, float)

    def test_power_tip(self):
        self.assertIsInstance(self.num, int)

    def test_return_something(self):
        self.assertIsNotNone(power(self.num,self.power))

    def test_return_tip(self):
        self.assertIsInstance(power(self.num,self.power),type(self.num))

    def test_invalid_num(self):
        message="Valoarea abc este invalida."
        self.assertEqual(power("abc",self.power),message)

    def test_invalid_power(self):
        message="Valoarea aleasa pentru 4.5 este invalida."
        self.assertEqual(power(self.num,4.5), message)

    def test_valid_return(self):
        self.assertEqual(power(self.num,self.power),self.num**self.power)

if __name__ == "__main__":
    unittest.main()