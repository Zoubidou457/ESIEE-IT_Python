import unittest
from password_generator import PasswordGenerator
import math

class TestPasswordGenerator(unittest.TestCase):
    
    def test_generate_password(self):
        # Tester si la longueur du mot de passe est correcte
        password = PasswordGenerator.generate_password(length=12, use_upper=True, use_digits=True, use_special=True)
        self.assertEqual(len(password), 12)

    def test_calculate_entropy(self):
        # Tester si l'entropie est supérieure à 0
        password = "aA1!"
        entropy = PasswordGenerator.calculate_entropy(password)
        self.assertGreater(entropy, 0)

    def test_entropy_for_12_characters(self):
        # Tester l'entropie pour un mot de passe de 12 caractères
        password = PasswordGenerator.generate_password(length=12, use_upper=True, use_digits=True, use_special=True)
        entropy = PasswordGenerator.calculate_entropy(password)
        
        # Estimation de l'entropie minimale (en fonction des caractères possibles)
        possible_chars = 26 + 26 + 10 + 32  # Lettres minuscules, majuscules, chiffres, et caractères spéciaux
        expected_entropy = 12 * math.log2(possible_chars)
        self.assertGreaterEqual(entropy, expected_entropy * 0.95)  # Vérifie si l'entropie est proche de l'estimée

if __name__ == "__main__":
    unittest.main()
