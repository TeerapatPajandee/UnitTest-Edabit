import unittest
import LettersSharedBetween2Words

class TestLettersSharedBetween2Words(unittest.TestCase):
    def test_LettersSharedBetween2Words(self):
        self.assertEqual(LettersSharedBetween2Words.shared_letters("apple", "meaty"), 2)
        self.assertEqual(LettersSharedBetween2Words.shared_letters("fan", "forsook"), 1)
        self.assertEqual(LettersSharedBetween2Words.shared_letters("spout", "shout"), 4)
        self.assertEqual(LettersSharedBetween2Words.shared_letters("took", "taken"), 2)
        self.assertEqual(LettersSharedBetween2Words.shared_letters("mentor", "terminal"), 5)
        self.assertEqual(LettersSharedBetween2Words.shared_letters("class", "last"), 3)

if __name__ == "__main__":
    unittest.main()