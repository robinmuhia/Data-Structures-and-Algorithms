from random_word import RandomWords
import string

player_wins = 0
player_losses = 0
all_letters = set(string.ascii_lowercase)
is_playing = True

name = input('Name: ').title()
print("Please type a letter to play or 1 to quit")
print('You only have 7 chances to guess the correct word')

while is_playing:
    try:
        lives = 7
        correct_word = RandomWords()
        randomized_word = correct_word.get_random_word()  # a random word        
        generated_word = randomized_word.lower()      
        generated_word_letters = set(x[0].lower() for x in generated_word)  # tabulates letters in the aforementioned word
        guessed_letters = set()  # input from the player
        
        for letter in generated_word_letters.copy():
            if letter not in all_letters:
                generated_word_letters.remove(letter)
                guessed_letters.add(letter)

        while True:
            correct_guessed_word = (letter if letter in guessed_letters else '_' for letter in generated_word)
            if set(generated_word) == set(correct_guessed_word):
                player_wins += 1
                print(f"Congratulations! You deciphered the word '{generated_word}' correctly!")
                print('Please type in a letter to continue playing or 1 to quit')
                break           
            elif lives == 0:
                player_losses += 1
                print('You have used up your 7 chances')
                print(f'The word was {generated_word}')
                print('Please type in a letter to continue playing or 1 to quit')
                break
            player_command = input('> ').lower()  # player letter input                        
            if player_command == '1':
                is_playing = False
                print('Game over')
                print(f'You deciphered the correct word {player_wins} times accurately')
                print(f'You deciphered the correct word {player_losses} times wrongly')
                win_percentage = round(player_wins/(player_wins + player_losses)*100)
                if player_wins > player_losses:
                    print(f"Congrats {name}! Your success rate was {win_percentage}%!")
                elif player_wins < player_losses:
                    print(f'You suck {name}! You success rate was {win_percentage}%')
                elif player_wins == player_losses:
                    print(f'You drew!')
                else:
                    print("Don't fret. You can play next time!")
                break
            elif lives > 0:
                correct_guessed_word = (letter if letter in guessed_letters else '_' for letter in generated_word)
                if player_command in (all_letters - guessed_letters):
                    guessed_letters.add(player_command)
                    if player_command in generated_word_letters:
                        generated_word_letters.remove(player_command)                  
                        print('Congratulations. You have uncovered one letter')
                        print('Current correct guessed word: ', ''.join(correct_guessed_word))
                    elif player_command not in generated_word_letters:
                        lives -= 1
                        if lives > 0:
                            print(f"You have lost one life. Remaining lives: {lives}")
                            print('You have used these letters: ', ''.join(guessed_letters))
                            print('Current correct guessed word: ', ''.join(correct_guessed_word))                
                elif player_command not in all_letters and player_command != '1':
                    print('Please type in a letter!')
                else:
                    print('You have already used that letter')
                    print('You have used these letters: ', ''.join(guessed_letters))
                    print('Current correct guessed word: ', ''.join(correct_guessed_word))
    except:        
        if (player_wins != 0) or (player_losses != 0):
            print('Please check your internet connection!')  
            print('Game over')
            win_percentage = round(player_wins/(player_wins + player_losses)*100)
            if player_wins > player_losses:
                print(f"Congrats {name}! Your success rate was {win_percentage}%!")
            elif player_wins < player_losses:
                print(f'You suck {name}! You success rate was {win_percentage}%')
            else:
                print(f'Your success rate was 50%!')          
            break
        else:
            print('Please check your internet connection!') 
            print("Don't fret. You can play next time!")   
        break
