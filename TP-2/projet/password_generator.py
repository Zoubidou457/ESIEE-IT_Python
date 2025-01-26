import string
import secrets
from math import log2

class PasswordGenerator:
    @staticmethod
    def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
        # Liste des caractères possibles
        characters = string.ascii_lowercase  # Par défaut, on utilise les minuscules
        if use_upper:
            characters += string.ascii_uppercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation

        if length < 4:
            raise ValueError("La longueur du mot de passe doit être d'au moins 4 caractères.")  # Minimum length

        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password

    @staticmethod
    def calculate_entropy(password):
        # Taille du jeu de caractères possible
        charset_size = 0
        if any(c in string.ascii_lowercase for c in password):
            charset_size += 26  # Lowercase letters
        if any(c in string.ascii_uppercase for c in password):
            charset_size += 26  # Uppercase letters
        if any(c in string.digits for c in password):
            charset_size += 10  # Digits
        if any(c in string.punctuation for c in password):
            charset_size += len(string.punctuation)  # Special characters

        # Si le jeu de caractères est valide
        if charset_size > 0:
            # Entropie = longueur du mot de passe * log2 (taille du jeu de caractères)
            return len(password) * log2(charset_size)
        else:
            return 0
