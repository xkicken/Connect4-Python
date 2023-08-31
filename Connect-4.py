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
board = create_board(9, 7)
display_board(board)