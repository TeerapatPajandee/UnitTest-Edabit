import unittest
import ValidatePin

class TestValidatePin(unittest.TestCase):
    def test_validate(self):
        tests = [
            ["123456",  True],
            ["4512a5", False],
            [""      , False],
            ["21904" , False],
            ["9451"  ,  True],
            ["213132",  True],
            [" 4520" , False],
            ["15632 ", False],
            ["000000",  True],
        ]
        for test in tests:
            self.assertEqual(ValidatePin.valid(test[0]), test[1])

if __name__ == "__main__":
    unittest.main()