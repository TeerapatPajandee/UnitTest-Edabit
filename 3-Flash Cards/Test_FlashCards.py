import unittest
import FlashCards

class TestFlashCards(unittest.TestCase):
    def test_FlashCards(self):
        self.assertEqual(FlashCards.flash([3, 'x', 7]) ,21)

if __name__ == "__main__":
    unittest.main()