with open("day06/input.txt") as file:
    groups = [
        [set(person) for person in group.split()] for group in file.read().split("\n\n")
    ]

print(sum(len(set.union(*group)) for group in groups))
print(sum(len(set.intersection(*group)) for group in groups))
