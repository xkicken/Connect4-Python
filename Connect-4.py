def create_board(width, height):
    width = max(4, min(width, 10))
    height = max(4, min(height, 10))
    
    row = "." * width
    board = [row for _ in range(height)]
    
    return board

def get_width(board):
    return len(board[0])

def display_board(board):
    print_string = ""
    for i in range(len(board)):
        temp = board[i]
        print_string = ""
        for x in temp:
            print_string += x + " "
        print_string = print_string.strip()
        print(f"|{print_string}|")
    divder = "-" * len(print_string)
    print(f"|{divder}|")
    for x in range(len(print_string)):
        print_string = print_string.replace(".", str(x), 1)
    print(f"|{print_string}|")

def stage_1(width, height):
    display_board(create_board(width, height))

def is_valid_column(board, column_name):
    valid_column = []
    for x in range(get_width(board)):
        valid_column.append(x)
    if column_name != '':
        if float(column_name) in valid_column:
            return True
    return False

def next_player(players, current_player):
    if current_player == players[0]:
        return players[1]
    elif current_player == players[1]:
        return players[0]
