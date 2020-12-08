with open("day01/input.txt") as file:
    v = set(map(int, file.readlines()))

for a in v:
    if (b := 2020 - a) in v:
        print(a * b)

for a in v:
    for b in v:
        if (c := 2020 - a - b) in v:
            print(a * b * c)
