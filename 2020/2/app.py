from pprint import pprint
f = open('input.txt', 'r')

input = f.readlines()
lines = list()
for line in input:
    lines.append(line.split())

for line in lines:
    line.append(line[0].split('-'))

valid_passwords = 0
for line in lines:
    count = 0
    letter_in_question = line[1][0]
    for letter in line[2]:
        if letter == letter_in_question:
            count += 1
    if count >= int(line[3][0]) and count <= int(line[3][1]):
        valid_passwords += 1

print("The number of valid passwords is: " +  str(valid_passwords))


valid_passwords = 0
for line in lines:
    count = 0
    letter_in_question = line[1][0]
    first_index = int(line[3][0]) - 1
    second_index = int(line[3][1]) - 1
    password = line[2]
    if password[first_index] == letter_in_question and password[second_index] !=letter_in_question:
        valid_passwords += 1
    elif password[first_index] != letter_in_question and password[second_index] == letter_in_question:
        valid_passwords += 1
    

print("The number of valid passwords with the 'real' policy is: " +  str(valid_passwords))
