import random

class PassphraseGenerator:
    def __init__(self, wordlist_path):
        self.wordlist_path = wordlist_path
        self.wordlist = self.load_wordlist()

    def load_wordlist(self):
        """Charge le fichier de mots et renvoie une liste de mots."""
        wordlist = []
        try:
            with open(self.wordlist_path, 'r', encoding='utf-8') as file:
                for line in file.readlines():
                    # Supprimer les espaces autour et ignorer les lignes vides
                    line = line.strip()
                    if line:  # Si la ligne n'est pas vide
                        parts = line.split()
                        if len(parts) > 1:  # Assurez-vous qu'il y a au moins 2 éléments (numéro et mot)
                            wordlist.append(parts[1])  # Ajouter le mot (le deuxième élément)
        except FileNotFoundError:
            print(f"Erreur : Le fichier {self.wordlist_path} est introuvable.")
        except Exception as e:
            print(f"Erreur lors du chargement du fichier : {e}")
        return wordlist

    def generate_passphrase(self, num_words):
        """Génère une passphrase aléatoire en choisissant des mots du wordlist."""
        if len(self.wordlist) == 0:
            raise ValueError("Le wordlist est vide. Impossible de générer une passphrase.")
        
        passphrase = ' '.join(random.choice(self.wordlist) for _ in range(num_words))
        return passphrase
