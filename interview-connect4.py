
num_of_cols = 7
num_of_rows = 6
num_of_sequence = 4
EMPTY = 0
game_over = False
board = [[EMPTY for x in range(num_of_cols)] for y in range(num_of_rows)]
COMPUTER_PLAYER = 2
players = [1, 2]
play_against_computer = False


def print_board():
    for item in reversed(board):
        print(item)


def play_as_computer(shape):
    col, row = choose_empty_cell()
    insert_disc(col, shape)
    return col, row


def choose_empty_cell():
    for row_index, row in enumerate(board):
        for col_index, value in enumerate(row):
            if value == EMPTY:
                return col_index, row_index


def player_play(player):
    if play_against_computer and player == COMPUTER_PLAYER:
        print('\ncomputer is playing\n')
        col, row = play_as_computer(player)
    else:
        message = '\nplayer ' + str(player) + ': insert disc\n'
        col = input(message)
        col = int(col) - 1
        row = insert_disc(col, player)

    if is_win(col, row, player):
        global game_over
        game_over = True
        print('player ' + str(player) + ' won')


def insert_disc(col, shape):
    for index, row in enumerate(board):
        if row[col] is EMPTY:
            board[index][col] = shape
            print_board()
            return index


def is_win(col, row, shape):
    if col is None or row is None:
        return False
    row_arr = board[row]
    start = max(0, col - num_of_sequence)
    counter = 0
    for i in row_arr[start:col + num_of_sequence]:
        if i == shape:
            counter += 1
            if counter == num_of_sequence:
                return True
        else:
            counter = 0
    return False


def get_player():
    player = players.pop(0)
    players.append(player)
    return player

if __name__ == "__main__":
    play_against_computer = True
    print_board()
    while not game_over:
        player_play(get_player())




