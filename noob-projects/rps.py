import random
computer_choices = ("rock", 'paper', 'scissors')
player_wins = 0
computer_wins = 0
draws = 0
is_playing = True

name = input('Name: ').title()
print("""Please type :
R-to choose rock
P-to choose paper
S-to choose scissors
Q-to quit the game""")

while is_playing:
    command = input('> ').lower()
    if command == 'q':
        is_playing = False
        print('Thanks for playing!')
        print(f"You won {player_wins} times")
        print(f"Computer won {computer_wins} times")
        print(f"You drew {draws} times with the computer")
        if player_wins > computer_wins:
            print(f'Congratulations,{name}! You defeated the computer!')
        elif computer_wins > player_wins:
            print(f'You suck,{name}! Computer won more times!')
        else:
            print('Game ends in a draw!')
        break
    possibilities = random.choice(computer_choices)
    print(f'Computer picked {possibilities}')
    if (command == 'r' and possibilities == 'scissors') or (command == 'p' and possibilities == 'rock') or (
            command == 's' and possibilities == 'paper'):
        player_wins += 1
        print('You won!')
    elif (command == 'r' and possibilities == 'paper') or (command == 'p' and possibilities == 'scissors') or (
            command == 's' and possibilities == 'rock'):
        computer_wins += 1
        print('You lose!')
    elif (command == 'r' and possibilities == 'rock') or (command == 'p' and possibilities == 'paper') or (
            command == 's' and possibilities == 'scissors'):
        draws += 1
        print('Draw!')
    else:
        print("Please input 'r','p' or 's' to play. Press 'q' to quit!")


