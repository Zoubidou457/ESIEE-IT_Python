import string
import secrets

class PasswordGenerator:
    @staticmethod
    def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
        # Création de la liste de caractères possibles
        characters = string.ascii_lowercase  # Par défaut, on utilise les minuscules
        if use_upper:
            characters += string.ascii_uppercase  # Ajout des majuscules si demandé
        if use_digits:
            characters += string.digits  # Ajout des chiffres si demandé
        if use_special:
            characters += string.punctuation  # Ajout des caractères spéciaux si demandé

        if length < 4:
            raise ValueError("La longueur du mot de passe doit être d'au moins 4 caractères.")  # Sécurité minimale

        # Générer le mot de passe en choisissant un caractère aléatoire à chaque position
        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password

    @staticmethod
    def calculate_entropy(password):
        # Calcul de l'entropie basée sur la diversité des caractères
        charset_size = 0
        if any(c in string.ascii_lowercase for c in password):
            charset_size += 26  # Taille de l'alphabet minuscule
        if any(c in string.ascii_uppercase for c in password):
            charset_size += 26  # Taille de l'alphabet majuscule
        if any(c in string.digits for c in password):
            charset_size += 10  # Taille des chiffres
        if any(c in string.punctuation for c in password):
            charset_size += len(string.punctuation)  # Taille des caractères spéciaux

        # Entropie = longueur du mot de passe * log2 du nombre de caractères possibles
        return len(password) * charset_size.bit_length()

def run_password_tool():
    print("Bienvenue dans le générateur et testeur de mots de passe!")

    while True:
        print("\nChoisissez une option:")
        print("1: Générer un mot de passe aléatoire")
        print("2: Tester l'entropie d'un mot de passe")
        print("3: Quitter le programme")

        choice = input("Votre choix: ").strip()

        if choice == "1":
            try:
                # Demander les préférences pour le mot de passe
                length = int(input("Longueur du mot de passe: "))
                use_upper = input("Inclure des majuscules? (o/n): ").lower() == 'o'
                use_digits = input("Inclure des chiffres? (o/n): ").lower() == 'o'
                use_special = input("Inclure des caractères spéciaux? (o/n): ").lower() == 'o'

                # Générer le mot de passe et calculer son entropie
                password = PasswordGenerator.generate_password(length, use_upper, use_digits, use_special)
                entropy = PasswordGenerator.calculate_entropy(password)

                # Afficher le mot de passe et son entropie
                print(f"\nMot de passe généré: {password}")
                print(f"Entropie: {entropy:.2f} bits")
            except ValueError as e:
                print(f"Erreur: {e}")

        elif choice == "2":
            password = input("Entrez le mot de passe à tester: ")
            entropy = PasswordGenerator.calculate_entropy(password)
            print(f"\nEntropie du mot de passe: {entropy:.2f} bits")

        elif choice == "3":
            print("Merci d'avoir utilisé le générateur de mots de passe. À bientôt!")
            break
        else:
            print("Choix invalide. Veuillez essayer à nouveau.")

if __name__ == "__main__":
    run_password_tool()