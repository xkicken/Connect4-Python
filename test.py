def create_board(width, height):
    width = max(4, min(width, 10))
    height = max(4, min(height, 10))
    
    row = "." * width
    board = [row for _ in range(height)]
    
    return board
b = create_board(20, 10)
print(b)
 	
