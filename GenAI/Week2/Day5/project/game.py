import random

class Game:
    def get_user_item(self):
        while True:
            user_input = input("Choisissez un élément (Pierre/Feuille/Ciseaux) : ").lower()
            if user_input in ['pierre', 'feuille', 'ciseaux']:
                return user_input
            print("Choix invalide. Veuillez choisir Pierre, Feuille ou Ciseaux.")

    def get_computer_item(self):
        computer_item = random.randint(1, 3)
        if computer_item == 1:
            return "pierre"
        elif computer_item == 2:
            return "feuille"
        else:
            return "ciseaux"
        
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return 'draw'
        winning_combinations = [('pierre', 'ciseaux'), ('feuille', 'pierre'), ('ciseaux', 'feuille')]
        if (user_item, computer_item) in winning_combinations:
            return 'win'
        return 'loss'

    def play(self):
        # Obtenir le choix de l'utilisateur
        user_item = self.get_user_item()
        
        # Obtenir le choix de l'ordinateur
        computer_item = self.get_computer_item()
        
        # Déterminer le résultat
        result = self.get_game_result(user_item, computer_item)
        
        # Afficher le résultat
        result_messages = {
            'win': f"Vous avez choisi {user_item}. L'ordinateur a choisi {computer_item}. Vous avez gagné !",
            'loss': f"Vous avez choisi {user_item}. L'ordinateur a choisi {computer_item}. Vous avez perdu !",
            'draw': f"Vous avez choisi {user_item}. L'ordinateur a choisi {computer_item}. Égalité !"
        }
        print(result_messages[result])
        
        # Retourner le résultat
        return result

# Test
game = Game()
resultat = game.play()  