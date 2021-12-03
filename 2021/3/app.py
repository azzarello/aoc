from pprint import pprint

f = open('input', 'r')

input = f.readlines()

gamma = list()
ep = list()

zeroc = int()
onec = int()

for i in range(12):
    zeroc = 0
    onec = 0
    for line in input:
        if line[i] == "1":
            onec += 1
        elif line[i] == "0":
            zeroc += 1
    if onec > zeroc:
        gamma.append("1")
        ep.append("0")
    else:
        gamma.append("0")
        ep.append("1")

gamma = int("".join(gamma), 2)
ep = int("".join(ep),2)
print(gamma * ep)

input1 = list(input)
input2 = list(input)


for i in range(12):
    zeroc = 0
    onec = 0
    for j in range(len(input1)):
        if input1[j][i] == "1":
            onec += 1
        elif input1[j][i] == "0":
            zeroc += 1
    if onec >= zeroc:
        keepval = "1"
    else:
        keepval = "0"
    # print(keepval)
    to_remove = list()
    for count, line in enumerate(input1):
        if line[i] != keepval:
            to_remove.append(line)
        # else:
        #     print(line, count)
    for el in to_remove:
        input1.remove(el)
    # pprint(to_remove)
    if len(input1) == 1:
        break
    # pprint(input1)
    # print("zc", zeroc)
    # print("oc", onec) 
    # print("kv", keepval) 
    # print(len(to_remove))
# pprint(input1)
print(len(input1))
og = int(input1[0], 2)

for i in range(12):
    zeroc = 0
    onec = 0
    for j in range(len(input2)):
        if input2[j][i] == "1":
            onec += 1
        elif input2[j][i] == "0":
            zeroc += 1
    if onec >= zeroc:
        keepval = "0"
    else:
        keepval = "1"
    # print(keepval)
    to_remove = list()
    for line in input2:
        if line[i] != keepval:
            to_remove.append(line)
    for el in to_remove:
        input2.remove(el)
    if len(input2) == 1:
        break
# pprint(input2)
print(len(input2))
co = int(input2[0], 2)

print(og) 
print(co) 
print()
print(og * co)



