import unittest
from interview import interview


class TestEncodeMorse(unittest.TestCase):
    def test_encode_morse(self):
        self.assertEqual(interview([5, 5, 10, 10, 15, 15, 20, 20], 120), "qualified")
        self.assertEqual(interview([2, 3, 8, 6, 5, 12, 10, 18], 120), "qualified")
        self.assertEqual(interview([2, 3, 8, 6, 5, 12, 10, 18], 64), "qualified")
        self.assertEqual(interview([5, 5, 10, 10, 25, 15, 20, 20], 120), "disqualified")
        self.assertEqual(interview([5, 5, 10, 10, 15, 15, 20], 120), "disqualified")
        self.assertEqual(interview([5, 5, 10, 10, 15, 15, 20, 20], 130), "disqualified")
        self.assertEqual(interview([5, 5, 10, 10, 15, 20, 50], 160), "disqualified")
        self.assertEqual(interview([5, 5, 10, 10, 15, 15, 40], 120), "disqualified")
        self.assertEqual(interview([10, 10, 15, 15, 20, 20], 150), "disqualified")
        self.assertEqual(interview([5, 5, 10, 20, 15, 15, 20, 20], 140), "disqualified")


if __name__ == "__main__":
    unittest.main()
