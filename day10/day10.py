import numpy as np
from collections import Counter, defaultdict

with open("day10/input.txt") as file:
    a = list(map(int, file.read().split("\n")))

a = sorted([0] + a + [max(a) + 3])
n = len(a)

c = Counter(np.diff(a))
print(c[1] * c[3])

# memo[i] is number of ways to reach a[i]
memo = defaultdict(int)
memo[n - 1] = 1
for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        if a[j] - a[i] <= 3:
            memo[i] += memo[j]
        else:
            break
print(memo[0])
