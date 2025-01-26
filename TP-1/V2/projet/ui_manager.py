import random
import tkinter as tk
from PIL import Image, ImageTk
from quiz_logic import get_questions

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz sur les jeux vidéo")
        self.root.geometry("900x800")  # Taille de la fenêtre élargie

        self.question_bank = get_questions()
        random.shuffle(self.question_bank)

        self.current_question_index = 0
        self.score = 0

        self.setup_ui()
        self.display_question()

    def setup_ui(self):
        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)

        self.question_label = tk.Label(self.root, text="", wraplength=700, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.options_var = tk.StringVar(value="")

        self.option_buttons = []
        for i in range(3):
            btn = tk.Radiobutton(self.root, text="", variable=self.options_var, value=f"{chr(97 + i)}", font=("Arial", 12))
            btn.pack(anchor="w", padx=20)
            self.option_buttons.append(btn)

        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 12), fg="green")
        self.feedback_label.pack(pady=10)

        self.submit_button = tk.Button(self.root, text="Soumettre", command=self.check_answer, font=("Arial", 12))
        self.submit_button.pack(pady=20)

    def display_question(self):
        question = self.question_bank[self.current_question_index]

        # Charger et redimensionner l'image
        image = Image.open(question.image_path)
        image.thumbnail((400, 400))  # Conserve les proportions tout en limitant la taille
        self.photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=self.photo)

        self.question_label.config(text=f"Question {self.current_question_index + 1}: {question.prompt}")
        
        for i, option in enumerate(question.options):
            self.option_buttons[i].config(text=option)

        self.options_var.set("")
        self.feedback_label.config(text="")

    def check_answer(self):
        selected_answer = self.options_var.get()
        if not selected_answer:
            self.feedback_label.config(text="Veuillez sélectionner une réponse !", fg="red")
            return

        question = self.question_bank[self.current_question_index]
        if question.is_correct(selected_answer):
            self.score += 1
            self.feedback_label.config(text="Bonne réponse !", fg="green")
        else:
            self.feedback_label.config(text=f"Mauvaise réponse ! La bonne réponse était : {question.correct_answer}.", fg="red")

        self.current_question_index += 1
        self.root.after(1500, self.next_question)

    def next_question(self):
        if self.current_question_index < len(self.question_bank):
            self.display_question()
        else:
            self.end_quiz()

    def end_quiz(self):
        self.feedback_label.config(text=f"Quiz terminé ! Votre score final : {self.score}/{len(self.question_bank)}.", fg="blue")
        self.submit_button.config(state="disabled")
