import unittest
from quiz_logic import QuizQuestion

class TestQuizLogic(unittest.TestCase):
    def test_is_correct(self):
        question = QuizQuestion(
            "Quel est le jeu vidéo le plus vendu de tous les temps ?",
            ["a) Minecraft", "b) Grand Theft Auto V", "c) Tetris"],
            "a",
            "images/minecraft.jpg"
        )
        self.assertTrue(question.is_correct("a"))
        self.assertFalse(question.is_correct("b"))
        self.assertFalse(question.is_correct("c"))

if __name__ == "__main__":
    unittest.main()
