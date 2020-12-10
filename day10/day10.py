import numpy as np
from collections import Counter
from functools import lru_cache

with open("day10/input.txt") as file:
    a = list(map(int, file.read().split("\n")))

a = sorted([0] + a + [max(a) + 3])
c = Counter(np.diff(a))
print(c[1] * c[3])

@lru_cache
def ways(i):
    if i == len(a) - 1:
        return 1
    return sum([ways(j) for j in range(i + 1, len(a)) if a[j] - a[i] <= 3])
print(ways(0))