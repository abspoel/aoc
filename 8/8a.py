prog = [(line.split()[0], int(line.split()[1])) for line in open("input")]
i = 0
execd = set()
acc = 0
while i not in execd:
    execd.add(i)
    inst, arg = prog[i]
    if inst == "nop":
        i += 1
    elif inst == "acc":
        acc += arg
        i += 1
    elif inst == "jmp":
        i += arg
    else:
        raise ValueError()
print(acc)
