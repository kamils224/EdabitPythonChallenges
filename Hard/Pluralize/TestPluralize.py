import unittest
from Pluralize import pluralize


class TestPluralize(unittest.TestCase):
    def test_pluralize(self):
        self.assertEqual(pluralize(["cow", "pig", "cow", "cow"]), {"cows", "pig"})
        self.assertEqual(pluralize(["table", "table", "table"]), {"tables"})
        self.assertEqual(
            pluralize(["chair", "pencil", "arm"]), {"chair", "pencil", "arm"}
        )
        self.assertEqual(pluralize(["list"]), {"list"})
        self.assertEqual(
            pluralize(
                [
                    "set",
                    "set",
                    "tuple",
                    "tuple",
                    "string",
                    "string",
                    "string",
                    "string",
                    "integer",
                ]
            ),
            {"sets", "tuples", "strings", "integer"},
        )


if __name__ == "__main__":
    unittest.main()
