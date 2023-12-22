def get_next_move(soduku):
    for i in range(9):  # This is for rowns
        for j in range(9):  # this is for columns
            if soduku[i][j] == 0:  # returns position of any available move if it is empty
                return i, j
    return None, None  # means that spot is filled.


def possible_move(soduku, allowed_number, i, j):
    row_numbers = soduku[
        i
    ]  # we index into this list first when indexing into the array so it will take the whole row
    if allowed_number in row_numbers:
        return False
    column_numbers = [
        soduku[i][j] for i in range(9)
    ]  # the double indexing here chooses the exact values and the for loop makes sure we go to the next iteration of the row
    if allowed_number in column_numbers:
        return False
    where_row_starts = (i // 3) * 3
    where_col_starts = (j // 3) * 3
    for i in range(where_row_starts, where_row_starts + 3):
        for j in range(where_col_starts, where_col_starts + 3):
            if allowed_number == soduku[i][j]:
                return False

    return True


def soduku_solver(soduku):
    i, j = get_next_move(soduku)  # i for row , j for column
    if i == None:
        return True

    for allowed_number in range(1, 10):  # choose btn 1-9
        if possible_move(soduku, allowed_number, i, j):
            soduku[i][j] = allowed_number
            if soduku_solver(soduku):
                return True

        soduku[i][j] = 0

    return False


def get_puzzle():
    print(
        """Type in entire rows.
    You should start from the first row at the top to the last one at the bottom.
    Input 0 (zer0) for the empty spaces in your puzzle
    Make sure that you put in 9 digits in each iteration of the row"""
    )
    mysoduku = []
    verifying_rows_are_nine = []

    for i in range(9):
        numbers = input(">")
        number_list = [int(i) for i in str(numbers)]
        mysoduku.append(number_list)
        verifying_rows_are_nine.append(len(number_list))

    if sum(verifying_rows_are_nine) == 81:
        return mysoduku

    return None


solving_puzzle = True
while solving_puzzle:
    try:
        puzzle_from_user = get_puzzle()
        if puzzle_from_user == None:
            print("Make sure you write in an entire row with nine values!")
            continue
        else:
            print(soduku_solver(puzzle_from_user))
            for line in puzzle_from_user:
                print(line)
            solving_puzzle = False
    except ValueError:
        print(
            "You will have to start again! Please be careful and make sure you are inputimg numbers only!"
        )
        continue
