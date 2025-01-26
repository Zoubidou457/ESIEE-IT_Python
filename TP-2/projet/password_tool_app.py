# password_tool_app.py
import tkinter as tk
from tkinter import ttk
from password_generator import PasswordGenerator  # Import du module PasswordGenerator


class PasswordToolApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Générateur de Mots de Passe")
        self.root.geometry("1500x1000")  # Fenêtre encore plus grande
        self.root.configure(bg="#f7f7f7")  # Background color

        # Style configuration
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#f7f7f7", foreground="#333333", font=("Arial", 12))
        style.configure("TButton", background="#3498db", foreground="white", font=("Arial", 10, "bold"), padding=10)
        style.configure("TCheckbutton", background="#f7f7f7", foreground="#333333", font=("Arial", 10))
        style.map("TButton", background=[("active", "#2980b9")])

        # Title
        self.title_label = ttk.Label(root, text="🔐 Générateur de Mots de Passe", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=40)

        # Frame for password generation
        self.gen_frame = ttk.LabelFrame(root, text="Options de génération", padding=20)
        self.gen_frame.pack(padx=40, pady=30, fill="x")

        # Length
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

        # Generate button
        self.generate_button = ttk.Button(self.gen_frame, text="Générer", command=self.generate_password)
        self.generate_button.grid(row=4, column=0, columnspan=2, pady=20)

        # Output for generated password
        self.generated_label = ttk.Label(root, text="Mot de passe généré:", font=("Arial", 14, "bold"))
        self.generated_label.pack(pady=20)

        # Change to tk.Entry for custom styling
        self.generated_password_var = tk.StringVar()
        self.generated_password_entry = tk.Entry(root, textvariable=self.generated_password_var, font=("Courier", 16),
                                                  justify="center", state="readonly", width=40, relief="solid", bd=2, 
                                                  bg="#ecf0f1", fg="#2c3e50")
        self.generated_password_entry.pack(pady=20)

        # Entropy and strength labels
        self.entropy_label = ttk.Label(root, text="", font=("Arial", 14, "bold"))
        self.entropy_label.pack(pady=10)

        self.strength_label = ttk.Label(root, text="", font=("Arial", 14, "bold"))
        self.strength_label.pack(pady=10)

        # Frame for entropy testing
        self.test_frame = ttk.LabelFrame(root, text="Tester l'entropie", padding=20)
        self.test_frame.pack(padx=40, pady=30, fill="x")

        # Password input for entropy
        self.test_label = ttk.Label(self.test_frame, text="Mot de passe:")
        self.test_label.grid(row=0, column=0, sticky="w", padx=20, pady=15)
        self.test_var = tk.StringVar()
        self.test_entry = ttk.Entry(self.test_frame, textvariable=self.test_var, font=("Courier", 14), width=30)
        self.test_entry.grid(row=0, column=1, padx=20, pady=15)

        # Test button
        self.test_button = ttk.Button(self.test_frame, text="Tester", command=self.test_entropy)
        self.test_button.grid(row=1, column=0, columnspan=2, pady=20)

    def generate_password(self):
        try:
            length = self.length_var.get()
            use_upper = self.upper_var.get()
            use_digits = self.digits_var.get()
            use_special = self.special_var.get()

            password = PasswordGenerator.generate_password(length, use_upper, use_digits, use_special)
            entropy = PasswordGenerator.calculate_entropy(password)
            strength = self.calculate_strength(entropy)

            # Update the generated password, its entropy, and its strength in the main window
            self.generated_password_var.set(password)
            self.entropy_label.config(text=f"Entropie: {entropy:.2f} bits", foreground="#3498db")
            self.strength_label.config(text=f"Force: {strength}", foreground="#2ecc71")

        except ValueError as e:
            self.entropy_label.config(text=f"Erreur: {str(e)}", foreground="red")

    def test_entropy(self):
        password = self.test_var.get()
        if not password:
            self.entropy_label.config(text="Erreur: Veuillez entrer un mot de passe.", foreground="red")
            return

        entropy = PasswordGenerator.calculate_entropy(password)
        strength = self.calculate_strength(entropy)
        self.entropy_label.config(text=f"Entropie: {entropy:.2f} bits", foreground="#3498db")
        self.strength_label.config(text=f"Force: {strength}", foreground="#2ecc71")

    def calculate_strength(self, entropy):
        """Calcule la force du mot de passe en fonction de son entropie."""
        if entropy < 40:
            return "Faible"
        elif 40 <= entropy < 80:
            return "Moyenne"
        else:
            return "Forte"
