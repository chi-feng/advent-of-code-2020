with open("day05/input.txt") as file:
    lines = file.readlines()

trans = str.maketrans("FBLR", "0101", "\n")
seats = {int(line.translate(trans), 2) for line in lines}

print(max(seats))

all = set(range(min(seats), max(seats)))
print((all - seats).pop())