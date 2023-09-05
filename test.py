def is_winner(board, player):
    if check_row(board,player) or check_column(board, player):
        return True
    else:
        return False

def check_column(board, player):
    count = 1
    for i in range(get_width(board)):
        temp_string = column_to_string(board, i)
        if temp_string.count(player) >= 4:
            for i in range(len(temp_string) - 1):
                if temp_string[i] == temp_string[i + 1] and temp_string[i] == player:
                    count += 1
        if count >= 4:
            return True
        count = 1
    return False

def check_row(board, player):
    count = 1
    for i in range(len(board)):
        temp_string = row_to_string(board, i)
        if temp_string.count(player) >= 4:
            for i in range(len(temp_string) - 1):
                if temp_string[i] == temp_string[i + 1] and temp_string[i] == player:
                    count += 1
        if count >= 4:
            return True
        count = 1
    return False

def get_width(board):
    return len(board[0])

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