from pprint import pprint


def check_for_win(board):
    for i in range(5):
        consecutive_count = 0
        for j in range(5):
            if board[j][i] == 1:
                consecutive_count += 1
        if consecutive_count == 5:
            return True
        consecutive_count = 0
        for j in range(5):
            if board[i][j] == 1:
                consecutive_count += 1
        if consecutive_count == 5:
            return True
    else:
        return False


f = open("input", "r")
input = f.readlines()

numbers = input[0].split(",")
num_boards = len(input) / 6
input.remove(input[0])
input.remove(input[0])
# pprint(input)
boards = list()
for i in range(num_boards):
    board = list()
    for j in range(5):
        row = input[i * 6 + j]
        board.append(row.split())
    boards.append(board)

hit_matrix = list()
for i in range(5):
    hit_matrix.append([0, 0, 0, 0, 0])

hit_matrices = list()
for i in range(num_boards):
    hit_matrices.append(hit_matrix)


# pprint(boards)
win = False
last_number = -1
um_sum = 0
num_count = 0
for num in numbers:
    for bnum, board in enumerate(boards):
        for i in range(5):
            for j in range(5):
                if board[i][j] == num:
                    hit_matrices[bnum][i][j] = 1
                    break
        if check_for_win(hit_matrices[bnum]):
            print(numbers)
            pprint(boards[bnum])
            pprint(hit_matrices[bnum])
            win = True
            last_number = int(num)
            for k in range(5):
                for l in range(5):
                    if hit_matrices[bnum][k][l] == 0:
                        um_sum += int(board[k][l])
            break
    if win == True:
        print(numbers[num_count])
        break
    num_count += 1
print(um_sum)
print(last_number)
print(um_sum * last_number)
print(530 * 4)
