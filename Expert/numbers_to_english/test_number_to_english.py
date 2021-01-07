import unittest
from numbers_to_english import num_to_eng

class TestNumbersToEnglish(unittest.TestCase):

    def test_numbers_to_english(self):
        self.assertEqual(num_to_eng(0), "zero")
        self.assertEqual(num_to_eng(26), "twenty six")
        self.assertEqual(num_to_eng(519), "five hundred nineteen")
        self.assertEqual(num_to_eng(106), "one hundred six")
        self.assertEqual(num_to_eng(999), "nine hundred ninety nine")


if __name__ == "__main__":
    unittest.main()