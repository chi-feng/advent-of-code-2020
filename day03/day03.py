import math

with open("day03/input.txt") as file:
    lines = file.read().split()

grid = [[1 if c == '#' else 0 for c in line] for line in lines]

h = len(grid)
w = len(grid[0])

counts = []
for dx, dy in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    x = 0
    y = 0
    trees = 0
    while y < h - 1:
        x = (x + dx) % w
        y = y + dy
        trees += grid[y][x]
    counts.append(trees)

print(math.prod(counts))
