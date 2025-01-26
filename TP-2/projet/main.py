import tkinter as tk
import os
import math
from tkinter import ttk
from password_generator import PasswordGenerator
from passphrase_generator import PassphraseGenerator

def calculate_entropy(password):
    # Calcul de l'entropie basée sur la longueur du mot de passe et le nombre de possibilités
    possible_chars = 0
    if any(c.islower() for c in password):
        possible_chars += 26  # Lettres minuscules
    if any(c.isupper() for c in password):
        possible_chars += 26  # Lettres majuscules
    if any(c.isdigit() for c in password):
        possible_chars += 10  # Chiffres
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?/`~" for c in password):
        possible_chars += 32  # Caractères spéciaux

    # Calcul de l'entropie en fonction du nombre de caractères et du nombre de possibilités
    entropy = len(password) * math.log2(possible_chars)
    return entropy

def get_password_strength(entropy):
    # Déterminer la force du mot de passe en fonction de l'entropie
    if entropy < 28:
        return "Faible", "red"
    elif entropy < 56:
        return "Moyenne", "orange"
    else:
        return "Forte", "green"

class PasswordToolApp:
    def __init__(self, root, wordlist_path):
        self.root = root
        self.root.title("Générateur de Mots de Passe et Passphrase")
        self.root.geometry("800x700")
        self.root.configure(bg="#f7f7f7")

        # PassphraseGenerator instance
        self.passphrase_generator = PassphraseGenerator(wordlist_path)

        # Title
        self.title_label = ttk.Label(root, text="🔐 Générateur de Mots de Passe", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=40)

        # Frame for password generation
        self.gen_frame = ttk.LabelFrame(root, text="Options de génération", padding=20)
        self.gen_frame.pack(padx=40, pady=30, fill="x")

        # Password Length
        self.length_label = ttk.Label(self.gen_frame, text="Longueur du mot de passe:")
        self.length_label.grid(row=0, column=0, sticky="w", padx=20, pady=15)
        self.length_var = tk.IntVar(value=12)
        self.length_entry = ttk.Entry(self.gen_frame, textvariable=self.length_var, width=5, font=("Arial", 14))
        self.length_entry.grid(row=0, column=1, padx=20, pady=15)

        # Checkboxes
        self.upper_var = tk.BooleanVar(value=True)
        self.upper_check = ttk.Checkbutton(self.gen_frame, text="Inclure des majuscules", variable=self.upper_var)
        self.upper_check.grid(row=1, column=0, columnspan=2, sticky="w", padx=20, pady=15)

        self.digits_var = tk.BooleanVar(value=True)
        self.digits_check = ttk.Checkbutton(self.gen_frame, text="Inclure des chiffres", variable=self.digits_var)
        self.digits_check.grid(row=2, column=0, columnspan=2, sticky="w", padx=20, pady=15)

        self.special_var = tk.BooleanVar(value=True)
        self.special_check = ttk.Checkbutton(self.gen_frame, text="Inclure des caractères spéciaux", variable=self.special_var)
        self.special_check.grid(row=3, column=0, columnspan=2, sticky="w", padx=20, pady=15)

        # Generate button for password
        self.generate_button = ttk.Button(self.gen_frame, text="Générer Mot de Passe", command=self.generate_password)
        self.generate_button.grid(row=4, column=0, columnspan=2, pady=20)

        # Output for generated password
        self.generated_label = ttk.Label(root, text="Mot de passe généré:", font=("Arial", 14, "bold"))
        self.generated_label.pack(pady=20)

        self.generated_password_var = tk.StringVar()
        self.generated_password_entry = tk.Entry(root, textvariable=self.generated_password_var, font=("Courier", 16),
                                                  justify="center", state="readonly", width=40, relief="solid", bd=2, 
                                                  bg="#ecf0f1", fg="#2c3e50")
        self.generated_password_entry.pack(pady=20)

        # Entropy result
        self.entropy_label = ttk.Label(root, text="", font=("Arial", 14, "bold"))
        self.entropy_label.pack(pady=20)

        # Strength result
        self.strength_label = ttk.Label(root, text="", font=("Arial", 14, "bold"))
        self.strength_label.pack(pady=10)

        # Frame for passphrase generation
        self.passphrase_frame = ttk.LabelFrame(root, text="Générer Passphrase", padding=20)
        self.passphrase_frame.pack(padx=40, pady=30, fill="x")

        # Number of words
        self.num_words_label = ttk.Label(self.passphrase_frame, text="Nombre de mots:")
        self.num_words_label.grid(row=0, column=0, sticky="w", padx=20, pady=15)
        self.num_words_var = tk.IntVar(value=6)
        self.num_words_entry = ttk.Entry(self.passphrase_frame, textvariable=self.num_words_var, width=5, font=("Arial", 14))
        self.num_words_entry.grid(row=0, column=1, padx=20, pady=15)

        # Generate button for passphrase
        self.generate_passphrase_button = ttk.Button(self.passphrase_frame, text="Générer Passphrase", command=self.generate_passphrase)
        self.generate_passphrase_button.grid(row=1, column=0, columnspan=2, pady=20)

        # Output for generated passphrase
        self.generated_passphrase_label = ttk.Label(root, text="Passphrase générée:", font=("Arial", 14, "bold"))
        self.generated_passphrase_label.pack(pady=20)

        self.generated_passphrase_var = tk.StringVar()
        self.generated_passphrase_entry = tk.Entry(root, textvariable=self.generated_passphrase_var, font=("Courier", 16),
                                                   justify="center", state="readonly", width=40, relief="solid", bd=2, 
                                                   bg="#ecf0f1", fg="#2c3e50")
        self.generated_passphrase_entry.pack(pady=20)

    def generate_password(self):
        try:
            length = self.length_var.get()
            use_upper = self.upper_var.get()
            use_digits = self.digits_var.get()
            use_special = self.special_var.get()

            # Générer le mot de passe
            password = PasswordGenerator.generate_password(length, use_upper, use_digits, use_special)
            
            # Calculer l'entropie
            entropy = calculate_entropy(password)

            # Afficher le mot de passe et l'entropie
            self.generated_password_var.set(password)
            self.entropy_label.config(text=f"Entropie: {entropy:.2f} bits", foreground="#3498db")

            # Calculer et afficher la force du mot de passe
            strength, color = get_password_strength(entropy)
            self.strength_label.config(text=f"Force: {strength}", foreground=color)
        except ValueError as e:
            self.entropy_label.config(text=f"Erreur: {str(e)}", foreground="red")

    def generate_passphrase(self):
        # Vérifier si le fichier existe avant de générer la passphrase
        if not os.path.exists(self.passphrase_generator.wordlist_path):
            self.generated_passphrase_var.set(f"Erreur : Fichier '{self.passphrase_generator.wordlist_path}' introuvable.")
        else:
            num_words = self.num_words_var.get()
            passphrase = self.passphrase_generator.generate_passphrase(num_words)
            
            # Calculer l'entropie pour la passphrase (calcul basé sur le nombre de mots et la taille du dictionnaire)
            entropy = calculate_entropy(passphrase)

            # Afficher la passphrase et son entropie
            self.generated_passphrase_var.set(passphrase)
            self.entropy_label.config(text=f"Entropie de la passphrase: {entropy:.2f} bits", foreground="#3498db")

if __name__ == "__main__":
    wordlist_dir = './wordlist/'  # Dossier relatif pour le fichier
    wordlist_path = os.path.join(wordlist_dir + "diceware_fr.txt")  # Chemin complet du fichier
    if not os.path.exists(wordlist_path):
        print(f"Le fichier {wordlist_path} est introuvable. Assurez-vous qu'il existe.")
    else:
        root = tk.Tk()
        app = PasswordToolApp(root, wordlist_path)
        root.mainloop()
