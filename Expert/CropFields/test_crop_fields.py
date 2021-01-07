import unittest
from crop_fields import crop_hydrated

class TestCropFields(unittest.TestCase):

    def test_crop_fields(self):

        self.assertEqual(crop_hydrated([
        [ "w", "w" ],
        [ "w", "c" ],
        [ "c", "c" ],
        [ "c", "w" ],
        [ "c", "w" ]
        ]), True)

        self.assertEqual(crop_hydrated([
        [ "c", "w", "w", "w", "c" ],
        [ "w", "c", "c", "c", "c" ],
        [ "c", "c", "c", "c", "c" ],
        [ "w", "c", "c", "w", "c" ]
        ]), True)

        self.assertEqual(crop_hydrated([
        [ "c", "w" ]
        ]), True)

        self.assertEqual(crop_hydrated([
        [ "w", "c", "c", "c", "c" ],
        [ "c", "c", "c", "w", "c" ]
        ]), True)

        self.assertEqual(crop_hydrated([
        [ "c", "c", "c" ],
        [ "w", "w", "c" ],
        [ "c", "c", "c" ],
        [ "w", "w", "c" ],
        [ "c", "c", "c" ],
        [ "c", "c", "c" ],
        [ "c", "w", "c" ]
        ]), True)

        self.assertEqual(crop_hydrated([
        [ "c", "c", "c" ],
        [ "w", "w", "c" ]
        ]), True)

        self.assertEqual(crop_hydrated([
        [ "c", "w", "w", "c", "c", "w", "c" ]
        ]), True)

        self.assertEqual(crop_hydrated([
        [ "c", "w", "c", "c", "w", "w" ],
        [ "c", "c", "w", "c", "c", "c" ],
        [ "w", "c", "c", "c", "c", "w" ],
        [ "c", "w", "c", "c", "c", "c" ],
        [ "c", "c", "c", "c", "w", "w" ]
        ]), True)

        self.assertEqual(crop_hydrated([
        [ "c" ],
        [ "w" ],
        [ "c" ],
        [ "c" ],
        [ "w" ],
        [ "c" ]
        ]), True)

        self.assertEqual(crop_hydrated([
        [ "c", "c", "w", "w", "c", "c", "c" ],
        [ "c", "w", "c", "w", "w", "c", "w" ],
        [ "w", "w", "c", "w", "c", "c", "c" ]
        ]), True)


        self.assertEqual(crop_hydrated([
        [ "c", "c", "w", "c", "c", "w", "c", "w" ]
        ]), False)

        self.assertEqual(crop_hydrated([
        [ "c", "c", "c", "c", "c", "w", "c" ],
        [ "c", "w", "c", "c", "w", "c", "w" ],
        [ "c", "c", "c", "w", "c", "w", "c" ],
        [ "w", "w", "c", "c", "c", "c", "c" ],
        [ "c", "c", "w", "c", "c", "c", "c" ],
        [ "c", "c", "c", "c", "w", "c", "c" ],
        [ "w", "c", "c", "c", "c", "c", "c" ],
        [ "c", "c", "c", "c", "c", "c", "c" ],
        [ "w", "c", "c", "c", "c", "c", "w" ]
        ]), False)

        self.assertEqual(crop_hydrated([
        [ "c", "w", "c", "c" ],
        [ "w", "c", "c", "c" ],
        [ "c", "c", "c", "c" ],
        [ "w", "c", "c", "c" ],
        [ "w", "w", "c", "c" ],
        [ "c", "w", "c", "c" ],
        [ "c", "c", "w", "c" ],
        [ "c", "c", "w", "w" ],
        [ "c", "c", "c", "w" ]
        ]), False)

        self.assertEqual(crop_hydrated([
        [ "c", "c", "c", "c", "c", "c" ],
        [ "c", "c", "c", "c", "c", "c" ],
        [ "w", "c", "c", "c", "c", "c" ],
        [ "c", "c", "c", "c", "c", "c" ],
        [ "c", "c", "c", "c", "c", "c" ],
        [ "c", "c", "c", "c", "c", "w" ],
        [ "c", "c", "c", "c", "w", "c" ],
        [ "c", "w", "w", "c", "c", "c" ]
        ]), False)

        self.assertEqual(crop_hydrated([
        [ "c", "c", "c", "c", "c", "w", "c" ],
        [ "w", "c", "c", "c", "c", "c", "w" ],
        [ "c", "c", "c", "c", "c", "c", "c" ],
        [ "c", "w", "w", "c", "c", "w", "w" ],
        [ "c", "c", "w", "c", "w", "c", "c" ],
        [ "w", "c", "c", "c", "w", "c", "c" ],
        [ "c", "c", "c", "c", "w", "c", "c" ],
        [ "w", "c", "c", "c", "c", "c", "c" ]
        ]), False)

        self.assertEqual(crop_hydrated([
        [ "c", "w", "c", "c", "w", "c", "c", "c", "w" ],
        [ "c", "c", "c", "c", "c", "c", "c", "c", "c" ],
        [ "w", "c", "c", "c", "w", "c", "c", "c", "c" ],
        [ "c", "c", "c", "c", "c", "w", "w", "w", "c" ],
        [ "w", "c", "c", "w", "w", "c", "c", "c", "w" ],
        [ "c", "c", "c", "c", "w", "c", "c", "c", "c" ],
        [ "c", "c", "c", "c", "c", "c", "c", "c", "c" ],
        [ "c", "c", "c", "c", "c", "c", "c", "c", "c" ]
        ]), False)

        self.assertEqual(crop_hydrated([
        [ "c", "c", "w", "c", "w" ],
        [ "c", "c", "c", "c", "c" ],
        [ "w", "c", "w", "c", "c" ],
        [ "c", "w", "w", "c", "c" ],
        [ "c", "c", "c", "c", "w" ],
        [ "c", "c", "c", "w", "c" ]
        ]), False)

        self.assertEqual(crop_hydrated([
        [ "c", "w", "c", "c", "c", "w", "w", "c" ],
        [ "c", "c", "c", "c", "c", "c", "c", "c" ],
        [ "c", "c", "c", "c", "c", "c", "c", "c" ],
        [ "c", "c", "c", "c", "c", "c", "c", "c" ],
        [ "w", "c", "c", "c", "c", "c", "w", "c" ]
        ]), False)

        self.assertEqual(crop_hydrated([
        [ "w", "w", "c", "c", "w" ],
        [ "c", "c", "c", "c", "c" ],
        [ "c", "c", "w", "c", "c" ],
        [ "w", "c", "c", "w", "w" ],
        [ "c", "c", "w", "c", "c" ],
        [ "c", "c", "w", "c", "c" ],
        [ "c", "c", "c", "w", "c" ]
        ]), False)

        self.assertEqual(crop_hydrated([
        [ "c", "c", "w", "c", "c", "w" ],
        [ "c", "w", "c", "c", "c", "c" ],
        [ "c", "c", "c", "c", "c", "c" ],
        [ "c", "c", "c", "w", "c", "c" ],
        [ "c", "c", "c", "c", "w", "c" ],
        [ "c", "c", "c", "c", "c", "c" ],
        [ "c", "c", "c", "c", "c", "c" ],
        [ "c", "c", "c", "c", "c", "c" ]
        ]), False)


if __name__ == "__main__":
    unittest.main()