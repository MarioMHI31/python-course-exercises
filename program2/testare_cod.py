import unittest
from cod import gaseste_numere
class TestNumere(unittest.TestCase):
    def setUp(self):
        self.numar1=2000
        self.numar2=3200

    def test_number1_exists(self):
        self.assertIsNotNone(self.numar1)

    def test_number2_exists(self):
        self.assertIsNotNone(self.numar2)

    def test_numar1_tip(self):
        self.assertIsInstance(self.numar1,int)

    def test_numar2_tip(self):
        self.assertIsInstance(self.numar2,int)

    def test_return_something(self):
        self.assertIsNotNone(gaseste_numere(self.numar1,self.numar2))

    def test_return_tip(self):
        self.assertIsInstance(gaseste_numere(self.numar1,self.numar2),list)

    def test_return_number_div_by_7(self):
        result=gaseste_numere(self.numar1,self.numar2)
        for num in result:
            self.assertTrue(num%7==0)

    def test_return_number_not_div_by_5(self):
        result=gaseste_numere(self.numar1,self.numar2)
        for num in result:
            self.assertFalse(num%5==0)

    def test_invalid_number1(self):
        message="Valoarea abc este invalida."
        self.assertEqual(gaseste_numere("abc",self.numar2),message)

    def test_invalid_number1(self):
        message="Valoarea def este invalida."
        self.assertEqual(gaseste_numere(self.numar1,"def"),message)