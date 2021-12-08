f = open('input.txt', 'r')
from pprint import pprint

input = f.readlines()
lines = list()
for line in input:
    lines.append(int(line))
pprint(lines)

count = 0
for i in range(len(lines) - 3):
    lower_window = lines[i]
    upper_window = lines[i + 3] 
    if lower_window < upper_window:
        count += 1

# for i in range(len(lines) - 1):
#     lower_window = lines[i]
#     upper_window = lines[i + 1] 
#     if lower_window < upper_window:
#         count += 1

print(count)
