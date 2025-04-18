import unittest

import string

from pyexpat.errors import messages

from cod_criptare import criptare

class TestCriptare(unittest.TestCase):
    def setUp(self):
        self.message= "abc"
        self.key= 1

    def test_message_exists(self):
        self.assertIsNotNone(self.message)

    def test_key_exists(self):
        self.assertIsNotNone(self.key)

    def test_message_tip(self):
        self.assertIsInstance(self.message,str)

    def test_key_tip(self):
        self.assertIsInstance(self.key,int)

    def test_message_len(self):
        self.assertGreater(len(self.message),0)

    def test_key_grater_than_0(self):
        self.assertGreater(self.key,0)

    def test_return_something(self):
        self.assertIsNotNone(criptare(self.message,self.key))

    def test_return_tip(self):
        self.assertIsInstance(criptare(self.message,self.key),str)

    def test_return_len(self):
        self.assertEqual(len(self.message),len(criptare(self.message,self.key)))

    def test_different_input_output(self):
        self.assertNotEqual(criptare(self.message,self.key),self.message)

    def test_out_of_range(self):
        chestii_posibile = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + " "
        self.assertNotEqual(criptare(chestii_posibile[-2:], self.key), chestii_posibile[-2:])



if __name__ == "__main__":
    unittest.main()