import numpy as np 
import sys

with open("day09/input.txt") as file:
    numbers = np.array(list(map(int, file.read().split("\n"))), dtype="int")

def can_sum(number, prev):
    for i in prev:
        if number - i in prev and number-i != i:
            return True
    return False

ans = 0
for i in range(25, len(numbers)):
    if not can_sum(numbers[i], set(numbers[i-25:i])):
        ans = numbers[i]
        break

print(ans)
    
for a in range(len(numbers)):
    for b in range(a, len(numbers)):
        span = numbers[a:b]
        s = np.sum(span)
        if s == ans:
            print(min(span) + max(span))
            sys.exit(0)
        if s > ans:
            break
