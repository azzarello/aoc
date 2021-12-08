from pprint import pprint

f = open("input", "r")
input = f.readlines()

lines = list()
for cp in input:
    cp_split = cp.replace("\n", "").split(" -> ")
    lines.append([cp_split[0].split(","), cp_split[1].split(",")])

hv_lines = list()
max_x = 0
max_y = 0
for line in lines:
    x1 = int(line[0][0])
    x2 = int(line[1][0])
    y1 = int(line[0][1])
    y2 = int(line[1][1])
    if x1 == x2 or y1 == y2:
        hv_lines.append(line)
    if x1 > max_x:
        max_x = x1
    elif x2 > max_x:
        max_x = x2
    if y1 > max_y:
        max_y = y1
    elif y2 > max_y:
        max_y = y2


board = list()
for i in range(max_y + 1):
    board.append([0] * (max_x + 1))

for line in lines:
    x1 = int(line[0][0])
    x2 = int(line[1][0])
    y1 = int(line[0][1])
    y2 = int(line[1][1])
    # print(line)
    lower_y = min(y1, y2)
    lower_x = min(x1, x2)
    if x1 == x2:
        higher_y = max(y1, y2)
        for i in range(abs(y2 - y1) + 1):
            board[lower_y + i][x1] += 1
    elif y1 == y2:
        higher_x = max(x1, x2)
        for i in range(abs(x1 - x2) + 1):
            board[y1][lower_x + i] += 1
    else:
        slope = (y2 - y1) // (x2 - x1)

        print(line)
        if x1 > x2 and y1 > y2:
            for i in range(abs(y2 - y1) + 1):
                print(f"board[{y2 + i}][{x2 + (i * slope)}]")
                board[y2 + i][x2 + (i * slope)] += 1
        elif x1 < x2 and y1 > y2:
            for i in range(abs(y2 - y1) + 1):
                print(f"board[{y1 + (i * slope)}][{x1 + i}]")
                board[y1 + (i * slope)][x1 + i] += 1
        elif x1 > x2 and y1 < y2:
            for i in range(abs(y2 - y1) + 1):
                print(f"board[{y2+ (i * slope)}][{x2+ i}]")
                board[y2 + (i * slope)][x2 + i] += 1
        elif x1 < x2 and y1 < y2:
            for i in range(abs(y2 - y1) + 1):
                print(f"board[{lower_y + i}][{lower_x + (i * slope)}]")
                board[y1 + i][x1 + (i * slope)] += 1


overlap_counter = 0
for line in board:
    for el in line:
        if el > 1:
            overlap_counter += 1
print(overlap_counter)
