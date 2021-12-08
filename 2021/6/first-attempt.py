f = open("input", "r")
input = f.readlines()

fish = input[0].replace("\n", "").split(",")
int_map = map(int, fish)
fish = list(int_map)


for _ in range(256):
    new_fish = list()
    print(_)
    for i in fish:
        if i == 0:
            new_fish.append(8)
            new_fish.append(6)
        else:
            new_fish.append(i - 1)
    fish = new_fish

print(len(fish))
