from pprint import pprint

f = open("input", "r")
input = f.readlines()

binary_map = {"B": "1", "F": "0", "L": "0", "R": "1"}


seat_ids = list()
for seat in input:
    binary = list()
    for position in seat.rstrip():
        binary.append(binary_map[(position)])
    seat_id = int("".join(binary), 2)
    seat_ids.append(seat_id)
print(max(seat_ids))


# seat_ids = seat_ids.sort()

story_guys_seat = -1
for seat_id in range(128 * 8):
    if seat_id - 1 in seat_ids and seat_id + 1 in seat_ids and seat_id not in seat_ids:
        story_guys_seat = seat_id
        break
print(story_guys_seat)
