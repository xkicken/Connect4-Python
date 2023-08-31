def create_board(width, height):
    count = 0
    broad_width = ""
    broad = []
    if width < 4:
        width = 4
    elif height < 4:
        height =4
    while count != width:
        count += 1
        broad_width = broad_width + "."
    count = 0
    while count != height:
        count += 1
        broad.append(broad_width)
    return broad
b = create_board(6, 7)
print(b)