import unittest
import FlashCards

class TestFlashCards(unittest.TestCase):
    def test_FlashCards(self):
        self.assertEqual(FlashCards.flash([3, 'x', 7]) ,21)
        self.assertEqual(FlashCards.flash([3, 'x', 7]), 21)
        self.assertEqual(FlashCards.flash([5, '+', 7]), 12)
        self.assertEqual(FlashCards.flash([10, '-', 9]), 1)
        self.assertEqual(FlashCards.flash([10, '/', 0]), None)
        self.assertEqual(FlashCards.flash([10, '/', 3]), 3.33)
        self.assertEqual(FlashCards.flash([2, 'x', 0]), 0)
        self.assertEqual(FlashCards.flash([0, '/', 5]), 0)
        self.assertEqual(FlashCards.flash([0, '+', 0]), 0)
        self.assertEqual(FlashCards.flash([0, '-', 0]), 0)
        self.assertEqual(FlashCards.flash([8, '-', 0]), 8)
        self.assertEqual(FlashCards.flash([0, '/', 0]), None)
        self.assertEqual(FlashCards.flash([3, '/', 8]), 0.38)

if __name__ == "__main__":
    unittest.main()