import unittest
from cod import verificare_expresie
class TestExpresie(unittest.TestCase):
    def setUp(self):
        self.expresie="abc"



    def test_expresion_exists(self):
        self.assertIsNotNone(self.expresie)

    def test_expresion_tip(self):
        self.assertIsInstance(self.expresie, str)

    def test_expresion_len(self):
        self.assertGreater(len(self.expresie), 0)

    def test_return_something(self):
        self.assertIsNotNone(verificare_expresie(self.expresie))

    def test_return_tip(self):
        self.assertIsInstance(verificare_expresie(self.expresie), bool)

    def test_paranteze_inchise_mai_multe(self):
        self.assertEqual(verificare_expresie("((5+3)*(7-2)+51))*(5"), False)

    def test_paranteze_deschise_mai_multe(self):
        self.assertEqual(verificare_expresie("((5+3)*(7-2)+51)*(5"), False)

    def test_paranteze_deschise_si_inchise_egale(self):
        self.assertEqual(verificare_expresie("((5+3)*(7-2)+51)*5"), True)







if __name__ == '__main__':
    unittest.main()