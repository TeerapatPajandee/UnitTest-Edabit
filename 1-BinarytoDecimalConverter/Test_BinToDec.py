import unittest
import BinToDec

class TestBinToDec(unittest.TestCase):
    def test_BinToDec(self):
        self.assertEqual(BinToDec.binary_to_decimal([1, 1, 1, 1, 1, 1, 1, 1]), 255)
        self.assertEqual(BinToDec.binary_to_decimal([0, 0, 0, 0, 0, 0, 0, 0]), 0)
        self.assertEqual(BinToDec.binary_to_decimal([1, 0, 1, 1, 1, 1, 0, 0]), 188)
        self.assertEqual(BinToDec.binary_to_decimal([1, 0, 1, 1, 0, 1, 0, 1]), 181)

if __name__ == "__main__":
    unittest.main()


    