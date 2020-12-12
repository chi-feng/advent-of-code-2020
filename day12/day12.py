import numpy as np

with open("day12/input.txt") as file:
    lines = [line.strip() for line in file.read().split("\n")]

instructions = [(line[0], int(line[1:])) for line in lines]

x = 0
y = 0
d = 0
delta = {
    0: (1, 0),
    1: (0, 1),
    2: (-1, 0),
    3: (0, -1)
}
for op, val in instructions:
    if op == 'F':
        dx, dy = delta[d]
        x += val * dx
        y += val * dy
    if op == 'N':
        y += val
    if op == 'E':
        x += val
    if op == 'S':
        y -= val
    if op == 'W':
        x -= val
    if op == 'R':
        d -= val // 90
    if op == 'L':
        d += val // 90
    d = d % 4

print(np.abs(x) + np.abs(y))

x, y = 0, 0
wx = 10
wy = 1
for op, val in instructions:
    if op == 'F':
        x += val * wx
        y += val * wy
    elif op == 'N':
        wy += val
    elif op == 'E':
        wx += val
    elif op == 'S':
        wy -= val
    elif op == 'W':
        wx -= val
    elif op == 'R':
        for i in range(val // 90):
            wx, wy = wy, -wx
    elif op == 'L':
        for i in range(val // 90):
            wx, wy = -wy, wx

print(np.abs(x) + np.abs(y))