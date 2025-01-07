import random

class Question:
    def __init__(self, texte, choix, reponse_correcte):
        self.texte = texte
        self.choix = choix
        self.reponse_correcte = reponse_correcte.lower()

    def verifier_reponse(self, reponse):
        return reponse.lower() == self.reponse_correcte


def lancer_qcm():
    # Liste des questions
    questions = [
        Question("Dans quel jeu rencontre-t-on le personnage de Mario pour la première fois ?",
                 ["a) Super Mario Bros", "b) Donkey Kong", "c) Mario Kart"], "b"),
        Question("Quel est le jeu vidéo le plus vendu de tous les temps ?",
                 ["a) Minecraft", "b) Grand Theft Auto V", "c) Tetris"], "a"),
        Question("Quel est le nom de l'arme iconique de Cloud dans Final Fantasy VII ?",
                 ["a) Gunblade", "b) Greatsword", "c) Buster Sword"], "c"),
        Question("Dans la série The Legend of Zelda, quel est le nom de la princesse kidnappée ?",
                 ["a) Zelda", "b) Peach", "c) Samus"], "a"),
        Question("Quel studio a développé The Witcher 3: Wild Hunt ?",
                 ["a) BioWare", "b) Bethesda", "c) CD Projekt Red"], "c"),
        Question("Dans Among Us, quel est le rôle des imposteurs ?",
                 ["a) Éliminer les autres joueurs", "b) Sauver l’équipage", "c) Réparer le vaisseau"], "a"),
        Question("Dans quel jeu combat-on des créatures appelées 'Heartless' ?",
                 ["a) Kingdom Hearts", "b) Dark Souls", "c) Final Fantasy"], "a"),
        Question("Quel Pokémon est connu comme étant le n°1 dans le Pokédex ?",
                 ["a) Pikachu", "b) Bulbizarre", "c) Salamèche"], "b"),
        Question("Quelle est la date de sortie originale de la première PlayStation ?",
                 ["a) 1994", "b) 1995", "c) 1993"], "a"),
        Question("Dans lequel de ces jeux peut-on incarner un chasseur de monstres dans un monde ouvert ?",
                 ["a) Skyrim", "b) World of Warcraft", "c) Monster Hunter"], "c"),
    ]

    random.shuffle(questions)  # Mélange les questions
    score = 0

    print("Bienvenue au QCM sur les jeux vidéo ! Répondez avec 'a', 'b' ou 'c'.\n")

    for index, question in enumerate(questions, start=1):
        print(f"Question {index}: {question.texte}")
        for choix in question.choix:
            print(choix)

        # Gestion des réponses utilisateur
        reponse = input("Votre réponse: ").strip().lower()
        while reponse not in {"a", "b", "c"}:
            reponse = input("Réponse invalide. Essayez encore les reponses possibles sont A B ou C : ").strip().lower()

        if question.verifier_reponse(reponse):
            print("Bonne réponse !\n")
            score += 1
        else:
            print(f"Mauvaise réponse ! La bonne réponse était : {question.reponse_correcte}\n")

    print(f"Votre score final : {score}/{len(questions)}. Merci d'avoir joué !")


if __name__ == "__main__":
    lancer_qcm()