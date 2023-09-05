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
    for i in reversed(range(len(board))):
        temp = board[i]
        print_string = ""
        for x in temp:
            print_string += x + " "
        print_string = print_string.strip()
        print(f"|{print_string}|")
    divder = "-" * len(print_string)
    print(f"|{divder}|")        
    print(f"|{column_name(board)}|")

def column_name(board):
    temp_string = ""
    for x in range(get_width(board)):
        temp_string += str(x) + " "
    temp_string = temp_string.strip()
    return temp_string        

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

def play_turn(board, player):
    valid_move = False
    while not valid_move:
        user_input = input(f"Player {player} -- enter the column: ")
        if user_input.isdigit() and is_valid_column(board, user_input) and is_valid_move(board, user_input):
            valid_move = True
        elif user_input == "quit":
            return "quit"
    return user_input

def play_game(board):
    count = 0
    current_player = "X"
    while count != 1:
        display_board(board)
        user_input = play_turn(board,current_player)
        if user_input == "quit":
            print(f"Result: player {current_player} quits!")
            count = 1
        else:
            add_piece_to_column(board, current_player, user_input)
            current_player = next_player("XO",current_player)

def is_valid_move(board, column_name):
    if board[-1][int(column_name)] == ".":
        return True
    return False

def column_contents(board, column_index):
    return_str = ""
    for x in board:
        return_str += x[column_index]
    return return_str

def get_free_row(board, column_index):
    count = -1
    temp_string = column_to_string(board, column_index)
    if temp_string.isalpha() == True:
        return -1
    else:
        for x in temp_string:
            if x == ".":
                count +=1
                return count
            if x != ".":
                count +=1

def modify_board(board, column_index, row_index, player):
    temp_string = str(board[int(row_index)])
    temp_string = temp_string[:int(column_index)] + player + temp_string[int(column_index) + 1:]
    board[int(row_index)] = temp_string

def add_piece_to_column(board, player, column_name):
    row_index = int(get_free_row(board, column_name))
    modify_board(board, column_name, row_index, player)

def is_full(board):
    count = 0
    for i in range(len(board)):
        if row_to_string(board, i).isalpha():
            count += 1
    if count == len(board):
        return True
    return False

def stage_1(width, height):
    display_board(create_board(width, height))

def stage_2(width, height):
    board = create_board(width, height)
    play_game(board)

def stage_3(width, height):
    board = create_board(width, height)
    play_game(board)

def row_to_string(list, index):
    temp_string = ""
    for x in list[int(index)]:
        temp_string += x
    return temp_string

def column_to_string(list, index):
    temp_string = ""
    for x in list:
        temp_string += x[int(index)]
    return temp_string
