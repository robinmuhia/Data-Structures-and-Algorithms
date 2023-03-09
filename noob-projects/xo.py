wins_tictactoe= 0
draws_tictactoe = 0
losses_tictactoe = 0


#the game's main core is from Kylie Ying. I struggled with this and i have to give credit to her. Nonetheless, I came to understand classes and functions deeply due to her. Whatever my career in software development comes to be, i would really like to thank her and freecodecamp.

import math
import random
import time


is_playing = True
name = input('Name:').title()    
player_choice = ''


class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = 4
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best



class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None    

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]  


        

def play(game,x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                    if (player_choice == 'X' and game.current_winner == 'X') or (player_choice == 'O' and game.current_winner == 'O'):
                        global wins_tictactoe
                        wins_tictactoe += 1
                    else:                    
                        global losses_tictactoe
                        losses_tictactoe += 1   
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')
        global draws_tictactoe
        draws_tictactoe += 1  




while is_playing:
    x_player = 0
    o_player = 0
    t= TicTacToe()

    print("Type 'X' to use X or 'O' to use O  or Q to quit")

    player_input = input('>').upper()

    if player_input == 'Q':
        if wins_tictactoe > 0 or draws_tictactoe or losses_tictactoe:
            is_playing = False
            print("Game over!") 
            print(f'You won {wins_tictactoe} times')   
            print(f'You drew {draws_tictactoe} times') 
            print(f'You lost {losses_tictactoe} times') 
            if wins_tictactoe > losses_tictactoe:
                print(f'Congratulations {name}. You defeated the computer more times!')
            elif losses_tictactoe > wins_tictactoe:
                print (f'You suck,{name}! You lost more times to the computer!')  
            else:
                print('You drew with the computer!')
            break
        else:
            is_playing = False
            print('Maybe next time')
            break
        break
    elif player_input == 'X':
        x_player = HumanPlayer('X')
        player_choice = 'X'
        print('Choose a difficulty. Input 1 for easy or 2 for hard')        
        player_difficulty = input('>')
        if player_difficulty == '1':
            o_player = RandomComputerPlayer('O')
            play(t,x_player,o_player,print_game=True)
        elif player_difficulty == '2':
            o_player = SmartComputerPlayer('O')
            play(t,x_player,o_player,print_game=True)
        else:
            print('Invalid number!. Please type 1 for easy or 2 for hard!')
            break       
    elif player_input == 'O':
        o_player = HumanPlayer('O')
        player_choice = 'O'
        print('Choose a difficulty. Input 1 for easy or 2 for hard')    
        player_difficulty = input('>')
        if player_difficulty == '1':
            x_player = RandomComputerPlayer('X')
            play(t,x_player,o_player,print_game=True)
        elif player_difficulty == '2':
            x_player = SmartComputerPlayer('X')
            play(t,x_player,o_player,print_game=True)
        else:
            print('Invalid number! Please type in 1 for easy or 2 for hard!')
    else:
        ('Invalid input! Please type in X to use x or O to use o')         











