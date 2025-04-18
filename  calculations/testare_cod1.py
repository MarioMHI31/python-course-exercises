import unittest
from cod1 import numarul_de_litere_si_cifre
class TestSentence(unittest.TestCase):
    def setUp(self):
        self.sentence="abc"

    def test_sentence_exists(self):
        self.assertIsNotNone(self.sentence)

    def test_sentence_tip(self):
        self.assertIsInstance(self.sentence,str)

    def test_sentence_len(self):
        self.assertGreater(len(self.sentence),0)

    def test_return_something(self):
        self.assertIsNotNone(numarul_de_litere_si_cifre(self.sentence))

    def test_return_tip(self):
        self.assertIsInstance(numarul_de_litere_si_cifre(self.sentence),str)

    def test_return_len(self):
        self.assertGreater(len(self.sentence),0)

    def test_only_numbers(self):
        expected_result="numarul cifrelor este: 3,numarul literelor este: 0"
        self.assertEqual(numarul_de_litere_si_cifre("123"),expected_result)

    def test_only_letters(self):
        expected_result="numarul cifrelor este: 0,numarul literelor este: 3"
        self.assertEqual(numarul_de_litere_si_cifre("abc"),expected_result)

    def test_special_characters(self):
        expected_result="numarul cifrelor este: 3,numarul literelor este: 10"
        self.assertEqual(numarul_de_litere_si_cifre("Hello world 123!"),expected_result)

















if __name__ =='__main__':
    unittest.main()