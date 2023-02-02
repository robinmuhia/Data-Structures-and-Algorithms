def collatz_conjecture(number):  
    if number % 2 == 0:
        return number / 2
    elif number % 2 == 1:
        return number * 3 + 1



checking_collatz = True   
while checking_collatz:
    print('Please type in a number below or q to quit:')
    command = (input('>'))
    if command == 'q' or command == 'Q':
        checking_collatz = False
        break
    try:
        number = int(command)
        print("Collatz sequence:")
        print(number)
        while (number != 1):
            number = collatz_conjecture(number)
            print(number)
        print('This number has satisfied the collatz conjencture')
    except:
        continue
        


        