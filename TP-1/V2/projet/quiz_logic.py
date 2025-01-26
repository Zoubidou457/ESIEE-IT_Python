class QuizQuestion:
    def __init__(self, prompt, options, correct_answer, image_path):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer.lower()
        self.image_path = image_path

    def is_correct(self, answer):
        return answer.lower() == self.correct_answer

def get_questions():
    return [
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
