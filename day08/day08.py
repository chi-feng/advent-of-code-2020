with open("day08/input.txt") as file:
    lines = file.read().split("\n")

instructions = list()
for line in lines:
    op, arg = line.split()
    instructions.append((op, int(arg)))


def run_until_loop_or_halt(instructions, flip=None):
    visited = set()
    ip = 0  # instruction pointer
    acc = 0  # accumulator
    while True:
        if ip in visited:
            return "loop", acc
        if ip >= len(instructions):
            return "halt", acc
        op, arg = instructions[ip]
        visited.add(ip)
        if ip == flip:
            op = "nop" if op == "jmp" else "jmp"
        if op == "nop":
            ip += 1
        elif op == "acc":
            acc += arg
            ip += 1
        elif op == "jmp":
            ip += arg


# part 1
status, acc = run_until_loop_or_halt(instructions)
print(acc)

# part 2
flips = {i for (i, (op, arg)) in enumerate(instructions) if op in {"nop", "jmp"}}
for flip in flips:
    status, acc = run_until_loop_or_halt(instructions, flip)
    if status == "halt":
        print(acc)
