def create_board(width, height):
    count = 0
    broad_width = ""
    broad = []
    if width < 4:
        width = 4
    elif width > 10:
        width = 10
    if height < 4:
        height =4
    elif height > 10:
        height = 10
    while count != width:
        count += 1
        broad_width = broad_width + "."
    count = 0
    while count != height:
        count += 1
        broad.append(broad_width)
    return broad
b = create_board(20, 10)
print(b)