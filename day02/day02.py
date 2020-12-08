import re

with open("day02/input.txt") as file:
    lines = file.readlines()

p1 = 0
p2 = 0
for line in lines:
    for (a, b, c, pw) in re.findall(r"(\d)-(\d) (.): (.+)", line):
        a = int(a)
        b = int(b)
        if a <= pw.count(c) <= b:
            p1 += 1
        if (pw[a - 1] == c) ^ (pw[b - 1] == c):
            p2 += 1

print(p1)
print(p2)
