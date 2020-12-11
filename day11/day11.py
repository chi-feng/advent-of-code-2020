from itertools import product

with open("day11/input.txt") as file:
    lines = [line.strip() for line in file.read().split("\n")]

w = len(lines[0])
h = len(lines)

grid = [c for c in "".join(lines)]  # store as 1-d array for easy copying

deltas = [(x, y) for x, y in product((-1, 0, 1), (-1, 0, 1)) if not (x == 0 and y == 0)]


def neighbors(grid, i, j):
    n = 0
    for dr, dc in deltas:
        r = i + dr
        c = j + dc
        if r in range(h) and c in range(w):
            if grid[r * w + c] == "#":
                n += 1
    return n


def visible(grid, i, j):
    n = 0
    for dr, dc in deltas:
        r, c = i, j
        while True:
            r += dr
            c += dc
            if r not in range(h) or c not in range(w):
                break
            if grid[r * w + c] == "L":
                break
            if grid[r * w + c] == "#":
                n += 1
                break
    return n


def step1(grid):
    new = grid.copy()
    for index, cell in enumerate(grid):
        row, col = index // w, index % w
        n = neighbors(grid, row, col)
        if cell == "L" and n == 0:
            new[index] = "#"
        if cell == "#" and n >= 4:
            new[index] = "L"
    return new


last = -1
while True:
    grid = step1(grid)
    count = grid.count("#")
    if count == last:
        print(count)
        break
    last = count


def step2(grid):
    new = grid.copy()
    for index, cell in enumerate(grid):
        row, col = index // w, index % w
        n = visible(grid, row, col)
        if cell == "L" and n == 0:
            new[index] = "#"
        if cell == "#" and n >= 5:
            new[index] = "L"
    return new


grid = [c for c in "".join(lines)]
last = -1
while True:
    grid = step2(grid)
    count = grid.count("#")
    if count == last:
        print(count)
        break
    last = count
