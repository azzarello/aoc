f = open('input.txt', 'r')
from pprint import pprint

input = f.readlines()
h_pos = 0
v_pos = 0
aim = 0

for line in input:
    split_line = line.split()
    command = split_line[0]
    x = int(split_line[1])
    if command == 'forward':
        h_pos += x
    elif command == 'down':
        v_pos += x
    elif command == 'up':
        v_pos -= x

print("The solution to part 1 of day 2 is: " + str(h_pos * v_pos))

h_pos = 0
v_pos = 0
aim = 0

for line in input:
    split_line = line.split()
    command = split_line[0]
    x = int(split_line[1])
    if command == 'forward':
        h_pos += x
        v_pos += aim * x
    elif command == 'down':
        aim += x
    elif command == 'up':
        aim -= x

print("The solution to part 2 of day 2 is: " + str(h_pos * v_pos))
