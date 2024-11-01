from abc import ABC, abstractmethod
import random

# Abstract Base Class for Game
class Game(ABC):
    def _init_(self, name):
        self.name = name
    
    @abstractmethod
    def play(self, player):
        pass

class DiceGame(Game):
    def _init_(self):
        super()._init_("Dice Game")
    
    def play(self, player):
        print(f"{player.name} is playing {self.name}. Rolling dice...")
        roll = random.randint(1, 6)
        print(f"{player.name} rolled a {roll}!")
        player.update_score(roll)
        return roll

class CardGame(Game):
    def _init_(self):
        super()._init_("Card Game")
    
    def play(self, player):
        print(f"{player.name} is playing {self.name}. Drawing card...")
        card_value = random.randint(1, 13)  # Assume 1-13 are card values
        print(f"{player.name} drew a card with value {card_value}!")
        player.update_score(card_value)
        return card_value

class Player:
    def _init_(self, name, age, player_id):
        self.name = name
        self.age = age
        self.player_id = player_id
        self.score = 0
    
    def update_score(self, points):
        self.score += points
        print(f"{self.name}'s new score: {self.score}")
    
    def get_score(self):
        return self.score

class GameSystem:
    def _init_(self):
        self.players = []
        self.games = [DiceGame(), CardGame()]

    def register_player(self):
        name = input("Enter player's name: ")
        age = int(input("Enter player's age: "))
        player_id = input("Enter player's ID: ")
        player = Player(name, age, player_id)
        self.players.append(player)
        print(f"Player {name} registered successfully!")
    
    def show_players(self):
        print("Registered players:")
        for player in self.players:
            print(f"- {player.name}, Age: {player.age}, Score: {player.get_score()}")

    def show_games(self):
        print("Available games:")
        for game in self.games:
            print(f"- {game.name}")

    def start_game(self):
        player_name = input("Enter the player's name who wants to play: ")
        game_name = input("Enter the game to play (Dice Game / Card Game): ")

        player = next((p for p in self.players if p.name == player_name), None)
        game = next((g for g in self.games if g.name == game_name), None)

        if player and game:
            game.play(player)
        else:
            print("Player or game not found. Please check the inputs.")

    def view_scores(self):
        print("Player Scores:")
        for player in self.players:
            print(f"{player.name}: {player.get_score()} points")

# Interactive menu
def main():
    system = GameSystem()

    while True:
        print("\n--- Game System Menu ---")
        print("1. Register a Player")
        print("2. Show All Players")
        print("3. Show All Games")
        print("4. Start a Game")
        print("5. View Player Scores")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == '1':
            system.register_player()
        elif choice == '2':
            system.show_players()
        elif choice == '3':
            system.show_games()
        elif choice == '4':
            system.start_game()
        elif choice == '5':
            system.view_scores()
        elif choice == '6':
            print("Exiting the game system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the game system
main()

"""
Player and Game Registration: Users can add players to the system, and games are predefined (e.g., Dice and Card games).
Dynamic Gameplay: Players can select a game and play, with scores updating based on random outcomes.
Score Tracking: The system keeps track of each player’s cumulative score, viewable at any time.
Interactive Menu: Provides a user-friendly, interactive menu to navigate the options easily.

Abstraction
The Game class is an abstract base class that defines a general structure for any game. 
By using the @abstractmethod decorator on play(), it mandates that all subclasses must implement this method, ensuring consistency across all game types.
This abstraction allows you to define the broad concept of a game without needing to specify how each game is played.
Each specific game (like DiceGame or CardGame) provides its own implementation of the play() method.

Encapsulation
Encapsulation is applied in the Player class, where the player’s score is updated through the update_score() method rather than directly. 
This keeps the score data encapsulated and protected, allowing controlled access and modification.
Additionally, GameSystem encapsulates the logic for managing players and games. 
For example, the register_player() and start_game() methods handle all interactions needed to add players and start games, keeping the details within the GameSystem class.
Inheritance
Inheritance is used to create specific game types (DiceGame and CardGame) that both inherit from the Game abstract base class.
Both DiceGame and CardGame automatically inherit the name attribute from the Game base class.
This relationship allows each subclass to share common functionality while also implementing unique game-specific behavior through the play() method.

Polymorphism is evident in the play() method of the DiceGame and CardGame classes. 
Even though both classes use the play() method, they implement it differently based on the type of game.
The GameSystem class can call play() on any game object without needing to know whether it is a DiceGame or CardGame, 
as each game type can execute its own version of play().
"""