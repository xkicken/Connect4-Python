def get_width(board):
    return len(board[0])
    
def is_valid_column(board, column_name):
    valid_column = []
    for x in range(get_width(board)):
        valid_column.append(x)
    if column_name != '':
        if float(column_name) in valid_column:
            return True
    return False
    
def is_valid_move(board, column_name):
    if board[-1][int(column_name)] == ".":
        return True
    return False
    
def play_turn(board, player):
    valid_move = False
    while not valid_move:
        user_input = input(f"Player {player} -- enter the column: ")
        if user_input.isdigit() and is_valid_column(board, user_input) and is_valid_move(board, user_input):
            valid_move = True
        elif user_input == "quit":
            return "quit"
    return user_input
    