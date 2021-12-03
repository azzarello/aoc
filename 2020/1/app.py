from itertools import combinations

f = open('input.txt', 'r')
lines = f.readlines()

nums = list()
for line in lines:
    nums.append(int(line))

combo = combinations(nums, 2) 

for i in list(combo):
    if i[0] + i[1] == 2020:
        print(i[0] * i[1])


combo3 = combinations(nums, 3) 

for i in list(combo3):
    if i[0] + i[1] + i[2] == 2020:
        print(i[0] * i[1] * i[2])
