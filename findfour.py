def main():
    print(f'''Welcome to Find Four!
---------------------''')
    index = 0
    h_or_w = ['height', 'width']
    row_or_col = ['rows', 'columns']
    height = 0
    width = 0
    while index < 2:  # Loop to get value from input, assigns it to height on first interation and width on second
        value_input = input(f'Enter {h_or_w[index]} of board ({row_or_col[index]}): ')
        try:
            value_input = int(value_input)
            if value_input < 4:
                print(f"Error: {h_or_w[index]} must be at least 4!")
            elif value_input > 25:
                print(f"Error: {h_or_w[index]} can be at most 25!")
            else:
                if index == 0:
                    height = value_input
                else:
                    width = value_input
                index += 1
                continue
        except ValueError:
            print("Error: not a number!")

    # Prints initial board
    board = get_initial_board(width, height)
    print_board(board)

    print("Player 1: x")
    print("Player 2: o")
    print()

    current_player = ['x', 'o']
    switch = 0
    # switch = 0: player 1 and 'x'
    # switch = 1: player 2 and 'o'
    # Main game loop
    while True:
        # Loop to check if inputted column is a number and within range
        while True:
            col = input(f"Player {switch + 1 } - Select a Column: ")
            try:
                col = int(col)
                if col < 0:
                    print('Error: no such column!')
                elif col > len(board[0]) - 1:
                    print('Error: no such column!')
                else:
                    row = insert_chip(board, col, current_player[switch])
                    if row == -1:
                        print('Error: column is full!')
                    else:
                        break
            except ValueError:
                print("Error: not a number!")
        print_board(board)
        if is_win_state(current_player[switch], board, row, col):
            print(f"Player {switch + 1} won the game!")
            quit()
        if is_board_full(board):
            print("Draw game! Players tied.")
            quit()
        # switches between player1 and player2
        if switch == 0:
            switch = 1
        else:
            switch = 0


def get_initial_board(rows, columns):
    board = [['.'] * rows for i in range(columns)]
    return board


def print_board(board):
    # print top row
    print(' ' + '__' * (len(board[0]) - 1) + '_')
    # print board
    for i in range(len(board) - 1, -1, -1):  # iterate backwards, as row 0 is the bottom
        print('|', end='')
        for j in range(0, len(board[0]) - 1):
            print(board[i][j], end=' ')
        print(board[i][len(board[0])-1], end='')
        print('|')
    # print bottom row
    print(' ' + '--' * (len(board[0]) - 1) + '-')
    print()


def insert_chip(board, column, chip):  # -> int
    # Places a chip in the column of the board of the chip type.
    # This method should find the next available spot in that column.
    # If any, this method returns the row in which the chip settles, returns -1 otherwise (column full).

    for row in range(0, len(board)):
        if board[row][column] == '.':
            board[row][column] = chip
            return row
    return -1


def is_win_state(chip, board, row, column):
    # This method checks if the player represented by specified chip type has won
    # the game by looking on the board at the position (row, column). If this is a win for the player, returns True;
    # otherwise, returns False.

    # Go as far down as you can until it hits an opposing chip
    lowest_row = row
    current_row = row
    while current_row >= 0 and board[current_row][column] == chip:
        lowest_row = current_row
        current_row -= 1
    # check if the lowest_row's chip is too close to the top
    if lowest_row + 3 < len(board):
        # check that the upper three are valid (have symbol that is chip)
        if board[lowest_row + 1][column] == chip \
                and board[lowest_row + 2][column] == chip \
                and board[lowest_row + 3][column] == chip:
            return True

    # Go as far left as you can until it hits an opposing chip
    leftmost_col = column
    current_col = column
    while current_col >= 0 and board[row][current_col] == chip:
        leftmost_col = current_col
        current_col -= 1
    # check if the leftmost_col's chip is too close to the right
    if leftmost_col + 3 < len(board[0]):
        # check that the rightmost three are valid (have symbol that is chip)
        if board[row][leftmost_col + 1] == chip \
                and board[row][leftmost_col + 2] == chip \
                and board[row][leftmost_col + 3] == chip:
            return True

    # if neither horizontal nor vertical searches found a win, return false.
    return False


def is_board_full(board: list[list[str]]):
    # This method checks if the board is full. If it is full, returns True; otherwise, returns False.
    for row in board:
        for space in row:
            if space == '.':
                return False
    return True


if __name__ == '__main__':
    main()
