import random


class RockPaperScissors:
    """Class that encapsulates core logic of rock, paper, scissors game"""

    def __init__(self) -> None:
        """Construtor for this class."""
        self.computer_choices = ("rock", "paper", "scissors")
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.name = ""
        self.player_choices = ("r", "p", "s", "q")

    def initialize_game(self) -> None:
        """Initialize the game."""
        name = input("name: ").title()
        print(
            """Please type :
        R-to choose rock
        P-to choose paper
        S-to choose scissors
        Q-to quit the game"""
        )
        self.name = name

    @staticmethod
    def get_player_command() -> str:
        """Get the player input."""
        player_command = input("> ").lower()
        return player_command

    def validate_player_input(self, player_command: str) -> bool:
        """Validate player chooses only r, p, s or q."""
        if player_command not in self.player_choices:
            print("Please input 'r','p' or 's' to play. Press 'q' to quit!")
            return False
        return True

    def end_game(self) -> None:
        """Ends the game and renders the stats"""
        print("Thanks for playing!")
        print(f"You won {self.wins} times")
        print(f"Computer won {self.losses} times")
        print(f"You drew {self.draws} times with the computer")
        if self.wins > self.losses:
            print(f"Congratulations,{self.name}! You defeated the computer!")
        elif self.losses > self.wins:
            print(f"You suck,{self.name}! Computer won more times!")
        else:
            print("Game ends in a draw!")

    def check_game_status(self, player_command: str) -> bool:
        """Check the game status incase the player quits."""
        if player_command == "q":
            return False
        return True

    def get_computer_move(self) -> str:
        computer_move = random.choice(self.computer_choices)
        return computer_move

    def game_logic(self, player_command: str, computer_move: str) -> None:
        """The core logic of this game"""
        print(f"Computer chose {computer_move}")
        if (
            (player_command == "r" and computer_move == "scissors")
            or (player_command == "p" and computer_move == "rock")
            or (player_command == "s" and computer_move == "paper")
        ):
            self.wins += 1
            print("You won!")
        elif (
            (player_command == "r" and computer_move == "paper")
            or (player_command == "p" and computer_move == "scissors")
            or (player_command == "s" and computer_move == "rock")
        ):
            self.losses += 1
            print("You lose!")
        else:
            self.draws += 1
            print("Draw!")

    def play(self) -> None:
        self.initialize_game()
        while True:
            player_command = self.get_player_command()
            is_move_valid = self.validate_player_input(player_command=player_command)
            if not is_move_valid:
                continue
            game_status = self.check_game_status(player_command=player_command)
            if not game_status:
                self.end_game()
                break
            computer_move = self.get_computer_move()
            self.game_logic(player_command=player_command, computer_move=computer_move)


RockPaperScissors().play()
