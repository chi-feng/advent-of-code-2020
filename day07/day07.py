import re
import collections
import functools

with open("day07/input.txt") as file:
    lines = file.read().split("\n")

parents_of = collections.defaultdict(set)
children_of = collections.defaultdict(list)

for line in lines:
    outer_color = re.match(r"([a-z\s]+) bags contain", line)[1]
    for count, inner_color in re.findall(r"(\d+) ([a-z\s]+) bags?[,.]", line):
        parents_of[inner_color].add(outer_color)
        children_of[outer_color].append((int(count), inner_color))

ancestors = set()


def add_ancestors_of(color):
    for color in parents_of[color]:
        ancestors.add(color)
        add_ancestors_of(color)


add_ancestors_of("shiny gold")
print(len(ancestors))


@functools.lru_cache
def cost(color):
    total = 0
    for count, inner_color in children_of[color]:
        total += count + count * cost(inner_color)
    return total


print(cost("shiny gold"))
print(cost.cache_info())
