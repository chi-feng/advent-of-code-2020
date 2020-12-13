import numpy as np

with open("day12/input.txt") as file:
    lines = [line.strip() for line in file.read().split("\n")]

instructions = [(line[0], int(line[1:])) for line in lines]

position = 0 + 0j
heading = 0 + 1j
directions = {"N": 1, "S": -1, "E": 1j, "W": -1j}
for command, value in instructions:
    if command == "F":
        position += value * heading
    elif command == "R":
        heading *= 1j ** (value // 90)
    elif command == "L":
        heading *= 1j ** (-value // 90)
    else:
        position += directions[command] * value
print(abs(position.real) + abs(position.imag))

position = 0 + 0j
waypoint = 1 + 10j
for command, value in instructions:
    if command == "F":
        position += value * waypoint
    elif command == "R":
        waypoint *= 1j ** (value // 90)
    elif command == "L":
        waypoint *= 1j ** (-value // 90)
    else:
        waypoint += directions[command] * value
print(abs(position.real) + abs(position.imag))