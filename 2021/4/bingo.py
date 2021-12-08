from pprint import pprint

def check_for_win(board, curr_num):
    for row in range(5):
        row_count = 0
        for column in range(5):
            row_count += board[row][column][1]
        if row_count == 5:
            return curr_num
    for column in range(5):
        column_count = 0
        for row in range(5):
            column_count += board[row][column][1]
        if column_count == 5:
            return curr_num
    return -1


f = open("input", "r")
input = f.readlines()

numbers = input[0].replace("\n", "").split(",")
numbers = [int(number) for number in numbers]

input.remove(input[0])
input.remove(input[0])

num_boards = len(input) / 5
input = [i.split() for i in input if i != "\n"]
for line in input:
    for i in range(5):
        line[i] = int(line[i])

boards = list()
for i in range(len(input) // 5):
    board = list()
    for j in range(5):
        board.append(input[i * 5 + j])
    boards.append(board)


def create_hit_matrices(boards):
    for board in boards:
        for i in range(5):
            for j in range(5):
                board[i][j] = (board[i][j], 0)
    return boards


boards = create_hit_matrices(boards)
# pprint(boards)


def run_game(boards, numbers):
    winning_boards = list()
    for n in numbers:
        for bn, b in enumerate(boards):
            if bn not in winning_boards:
                for row in range(5):
                    for col in range(5):
                        if b[row][col][0] == n:
                            b[row][col] = (b[row][col][0], 1)
                curr_num = check_for_win(b, n)
                if curr_num > -1:
                    if len(winning_boards) + 1 == len(boards):
                        return boards, curr_num, bn
                    winning_boards.append(bn)

def create_score(winning_board, final_num):
    um_count = 0
    for row in range(5):
        for col in range(5):
            if winning_board[row][col][1] == 0:
                um_count += winning_board[row][col][0]
    return um_count * final_num
            

winning_boards, final_num, winning_bn = run_game(boards, numbers)
final_score = create_score(winning_boards[winning_bn], final_num)

pprint(winning_boards[winning_bn])
print(final_num)
print(final_score)
                                    
