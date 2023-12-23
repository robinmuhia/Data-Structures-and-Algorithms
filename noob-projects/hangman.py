import string
from typing import Tuple

from random_word import RandomWords


class Hangman:
    """Class that encapsulates the core logic of the hangman game."""

    def __init__(self) -> None:
        """Constructor for the class."""
        self.wins = 0
        self.losses = 0
        self.lives = 7
        self.name = ""
        self.random_word = ""
        self.all_letters = set(string.ascii_lowercase)
        self.player_commands = set()
        self.random_word_letters = set()

    def initialize_game(self) -> None:
        """Get the name of the player"""
        name = input("Name: ").title()
        print("Please type a letter to play or 1 to quit")
        print("You only have 7 chances to guess the correct word")
        self.name = name

    def get_game_letters(self) -> None:
        """Get the game letters to play the game."""
        word = RandomWords()
        random_word: str = word.get_random_word()
        self.random_word = random_word
        self.random_word_letters = set(x[0].lower() for x in random_word)
        for letter in self.random_word_letters.copy():
            if letter not in self.all_letters:
                self.random_word_letters.remove(letter)
                self.random_word_letters.add(letter)

    def check_game_status(self) -> None:
        """Check whether players lives have exhausted or if player has won"""
        if self.lives <= 0:
            self.losses += 1
            print("You have used up your 7 chances")
            print(f"The word was {self.random_word}")
            print("Please type in a letter to continue playing or 1 to quit")
            self.reset_game()
        if set(self.random_word) == set(self.get_correct_guessed_word()):
            self.wins += 1
            print(f"Congratulations! You deciphered the word '{self.random_word}' correctly!")
            print("Please type in a letter to continue playing or 1 to quit")
            self.reset_game()

    def get_player_command(self) -> Tuple[bool, str]:
        """Get a player command."""
        player_command = input("> ")
        try:
            player_command = int(player_command)
            return False, player_command
        except ValueError:
            return True, player_command.lower()

    def end_game(self) -> None:
        """Ends the game and shows stats."""
        print("Game over")
        print(f"You deciphered the correct word {self.wins} times accurately")
        print(f"You deciphered the correct word {self.losses} times wrongly")

        try:
            win_percentage = round(self.wins / (self.wins + self.losses) * 100)
        except ZeroDivisionError:
            win_percentage = 0

        if self.wins > self.losses:
            print(f"Congrats {self.name}! Your success rate was {win_percentage}%!")
        elif self.wins < self.losses:
            print(f"You suck {self.name}! You success rate was {win_percentage}%")
        elif self.wins == self.losses:
            print(f"Meeeeh, your success rate was {win_percentage}%")
        else:
            print("Don't fret. You can play next time!")

    def get_correct_guessed_word(self) -> str:
        """Get the guessed correct word,
        put '_' in position for unguessed letters.
        """
        correct_guessed_word = (
            letter if letter in self.player_commands else "_" for letter in self.random_word
        )
        return correct_guessed_word

    def check_player_input(self, player_command: str) -> bool:
        """Validate player input."""
        if player_command not in self.all_letters and player_command != 1:
            print("Please type in a letter!")
            return False
        return True

    def game_logic(self, player_command: str) -> None:
        """Main logic for the game."""
        correct_guessed_word = self.get_correct_guessed_word()
        guessed_letters = self.player_commands
        if player_command not in guessed_letters and player_command in self.all_letters:
            self.player_commands.add(player_command)
            if player_command in self.random_word_letters:
                self.random_word_letters.remove(player_command)
                print("Congratulations. You have uncovered one letter")
                print("Current correct guessed word: ", "".join(correct_guessed_word))
            elif player_command not in self.random_word_letters:
                self.lives -= 1
                if self.lives > 0:
                    print(f"You have lost one life. Remaining lives: {self.lives}")
                    print("You have used these letters: ", "".join(guessed_letters))
                    print("Current correct guessed word: ", "".join(correct_guessed_word))
        else:
            print("You have already used that letter")
            print("You have used these letters: ", "".join(guessed_letters))
            print("Current correct guessed word: ", "".join(correct_guessed_word))

    def reset_game(self) -> None:
        """Resets the game in case of win or loss."""
        self.lives = 7
        self.all_letters = set(string.ascii_lowercase)
        self.player_commands = set()
        self.get_game_letters()

    def play(self) -> None:
        """Starts the game for you to play."""
        self.initialize_game()
        self.get_game_letters()
        while True:
            self.check_game_status()
            state, player_command = self.get_player_command()
            is_move_valid = self.check_player_input(player_command=player_command)
            if not is_move_valid:
                continue
            if not state:
                self.end_game()
                break
            self.game_logic(player_command=player_command)
