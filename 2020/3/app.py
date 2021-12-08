from pprint import pprint

f = open('input.txt', 'r')
input = f.readlines()

pprint(input)

product = 1
slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
for y, x in slopes:
    hit_count = 0
    for i in range(len(input) / y):
        if input[i * y][(x * i) % (len(input[0]) - 1)] == "#":
            hit_count += 1
    product *= hit_count
    print(y, x, hit_count)
print("product", product)
