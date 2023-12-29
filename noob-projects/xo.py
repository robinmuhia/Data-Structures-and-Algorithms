import math
import random
import time
from abc import ABC, abstractmethod
from typing import Dict, List


class TicTacToe:
    """Class for a TicTacToe game."""

    def __init__(self):
        """Constructor for this class."""
        self.board = self.make_board()
        self.current_winner: str | None = None

    @staticmethod
    def make_board() -> List[str]:
        """Makes the board for a player to play in."""
        return [" " for _ in range(9)]

    def print_board(self) -> None:
        """Prints the board to a user for viewing."""
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums() -> None:
        """Prints the numbers on the board"""
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def make_move(self, square, letter) -> bool:
        """Functionality that makes the intended legal move."""
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter) -> bool:
        """Finds out whether a player has won the game."""
        row_ind = math.floor(square / 3)
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self) -> List[str]:
        """Puts empty spaces in board."""
        return " " in self.board

    def num_empty_squares(self) -> int:
        """Calculates number of empty spaces on the board."""
        return self.board.count(" ")

    def available_moves(self):
        """Returns a list of all availabe legal moves."""
        return [i for i, x in enumerate(self.board) if x == " "]


class Player(ABC):
    """Instantiate a standard player."""

    def __init__(self, letter: str):
        self.letter = letter

    @abstractmethod
    def get_move(self, game: TicTacToe):
        """Base functionality to get a legal move"""
        pass


class HumanPlayer(Player):
    """Class for a human player"""

    def __init__(self, letter: str):
        """Constructor for a human player."""
        super().__init__(letter)

    def get_move(self, game) -> int:
        """Gets a move from a player and validates it."""
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val


class RandomComputerPlayer(Player):
    """Class for a computer making random moves."""

    def __init__(self, letter: str):
        """Constructor for the human class."""
        super().__init__(letter)

    def get_move(self, game):
        """Randomnly gets a move from the available moves."""
        square = random.choice(game.available_moves())
        return square


class SmartComputerPlayer(Player):
    """Class for a smart computer player."""

    def __init__(self, letter: str):
        super().__init__(letter)

    def get_move(self, game):
        """Implements a minimax algorithm to get the best move possible."""
        if len(game.available_moves()) == 9:
            square = 4
        else:
            square = self.minimax(game, self.letter)["position"]
        return square

    def minimax(self, state: TicTacToe, player: Player) -> dict[str:int]:
        """Implemenation of the minimax algorithm."""
        max_player = self.letter  # yourself
        other_player = "O" if player == "X" else "X"

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {
                "position": None,
                "score": 1 * (state.num_empty_squares() + 1)
                if other_player == max_player
                else -1 * (state.num_empty_squares() + 1),
            }
        elif not state.empty_squares():
            return {"position": None, "score": 0}

        if player == max_player:
            best = {"position": None, "score": -math.inf}  # each score should maximize
        else:
            best = {"position": None, "score": math.inf}  # each score should minimize
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = " "
            state.current_winner = None
            sim_score["position"] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score["score"] > best["score"]:
                    best = sim_score
            else:
                if sim_score["score"] < best["score"]:
                    best = sim_score
        return best


class PlayGame:
    """Instantiate this class and play a tictactoe game"""

    def play(
        self,
        game: TicTacToe,
        human_player: Player,
        computer_player: Player,
        score: dict[str, int],
        player_choice: str,
        print_game=True,
    ):
        """Starts the game"""

        if print_game:
            game.print_board_nums()

        if human_player.letter == "X":
            x_player = human_player
            o_player = computer_player
        else:
            x_player = computer_player
            o_player = human_player

        letter = "X"
        while game.empty_squares():
            if letter == "O":
                square = o_player.get_move(game)
            else:
                square = x_player.get_move(game)
            if game.make_move(square, letter):
                if print_game:
                    print(letter + " makes a move to square {}".format(square))
                    game.print_board()
                    print("")

                if game.current_winner:
                    if print_game:
                        print(letter + " wins!")
                        if (player_choice == "X" and game.current_winner == "X") or (
                            player_choice == "O" and game.current_winner == "O"
                        ):
                            score["wins"] += 1
                        else:
                            score["loss"] += 1
                    return letter  # ends the loop and exits the game
                letter = "O" if letter == "X" else "X"  # switches player

            time.sleep(0.8)

        if print_game:
            print("It's a tie!")
            score["draw"] += 1

    def choose_letter(self) -> str:
        """Choose letter to play with."""
        choices = ["X", "O", "Q"]

        print("Type 'X' to use X or 'O' to use O or 'Q' to quit")
        while True:
            player_input = input(">").upper()

            if player_input in choices:
                return player_input
            else:
                print("Invalid input! Please enter X, O, or Q.")

    def choose_difficulty(self) -> int:
        """Choose the difficulty you want to play, i.e., smart player or random player."""
        choices = [1, 2]
        print("Choose a difficulty. Input 1 for easy or 2 for hard")
        while True:
            difficulty = input(">")

            try:
                difficulty = int(difficulty)
                if difficulty in choices:
                    return difficulty
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid choice. Please enter 1 or 2.")

    @staticmethod
    def boot_game(player_input: str, diffculty: int):
        """Boots up the game."""
        human_player = HumanPlayer(player_input)
        computer_letter = "X" if player_input == "O" else "O"
        if diffculty == 1:
            computer_player = RandomComputerPlayer(computer_letter)
        else:
            computer_player = SmartComputerPlayer(computer_letter)
        return human_player, computer_player

    def start_game(self, score: Dict[str, int], name: str) -> None:
        """Starts a game instance"""
        wins = score["wins"]
        loss = score["loss"]
        draw = score["draw"]

        game = TicTacToe()
        chosen_letter = self.choose_letter()

        if chosen_letter == "Q":
            if wins > 0 or draw or loss:
                print("Game over!")
                print(f"You won {wins} times")
                print(f"You drew {draw} times")
                print(f"You lost {loss} times")
                if wins > loss:
                    print(f"Congratulations {name}. You defeated the computer more times!")
                elif loss > wins:
                    print(f"You suck,{name}! You lost more times to the computer!")
                else:
                    print("You drew with the computer!")
            else:
                print("Maybe next time")
            return

        difficulty = self.choose_difficulty()
        human_player, computer_player = self.boot_game(chosen_letter, difficulty)
        self.play(
            game=game,
            human_player=human_player,
            computer_player=computer_player,
            score=score,
            player_choice=chosen_letter,
        )
        return self.start_game(score=score, name=name)

    def play_multilple_games(
        self,
        score={
            "wins": 0,
            "loss": 0,
            "draw": 0,
        },
    ) -> None:
        """Start this to play multiple tictactoe games."""
        name = input("Name:").title()
        self.start_game(score=score, name=name)


PlayGame().play_multilple_games()
