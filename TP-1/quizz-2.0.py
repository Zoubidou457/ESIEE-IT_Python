import random
import tkinter as tk
from PIL import Image, ImageTk

class QuizQuestion:
    def __init__(self, prompt, options, correct_answer, image_path):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer.lower()
        self.image_path = image_path

    def is_correct(self, answer):
        return answer.lower() == self.correct_answer

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz sur les jeux vidéo")
        self.root.geometry("800x800")
        
        self.question_bank = [
            QuizQuestion("Dans quel jeu rencontre-t-on le personnage de Mario pour la première fois ?",
                         ["a) Super Mario Bros", "b) Donkey Kong", "c) Mario Kart"], "b", "images/donkey_kong.jpg"),
            QuizQuestion("Quel est le jeu vidéo le plus vendu de tous les temps ?",
                         ["a) Minecraft", "b) Grand Theft Auto V", "c) Tetris"], "a", "images/minecraft.jpg"),
            QuizQuestion("Quel est le nom de l'arme iconique de Cloud dans Final Fantasy VII ?",
                         ["a) Gunblade", "b) Greatsword", "c) Buster Sword"], "c", "images/cloud.jpg"),
            QuizQuestion("Dans la série The Legend of Zelda, quel est le nom de la princesse kidnappée ?",
                         ["a) Zelda", "b) Peach", "c) Samus"], "a", "images/zelda.jpg"),
            QuizQuestion("Quel studio a développé The Witcher 3: Wild Hunt ?",
                         ["a) BioWare", "b) Bethesda", "c) CD Projekt Red"], "c", "images/witcher.jpg"),
            QuizQuestion("Dans Among Us, quel est le rôle des imposteurs ?",
                         ["a) Éliminer les autres joueurs", "b) Sauver l’équipage", "c) Réparer le vaisseau"], "a", "images/among_us.jpg"),
            QuizQuestion("Dans quel jeu combat-on des créatures appelées 'Heartless' ?",
                         ["a) Kingdom Hearts", "b) Dark Souls", "c) Final Fantasy"], "a", "images/kingdom_hearts.jpg"),
            QuizQuestion("Quel Pokémon est connu comme étant le n°1 dans le Pokédex ?",
                         ["a) Pikachu", "b) Bulbizarre", "c) Salamèche"], "b", "images/bulbizarre.jpg"),
            QuizQuestion("Quelle est la date de sortie originale de la première PlayStation ?",
                         ["a) 1994", "b) 1995", "c) 1993"], "a", "images/playstation.jpg"),
            QuizQuestion("Dans lequel de ces jeux peut-on incarner un chasseur de monstres dans un monde ouvert ?",
                         ["a) Skyrim", "b) World of Warcraft", "c) Monster Hunter"], "c", "images/monster_hunter.jpg"),
        ]
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

        # Load and display image
        image = Image.open(question.image_path)
        image.thumbnail((400, 400))  # Keep aspect ratio and ensure the image fits in the 400x400 box
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

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()