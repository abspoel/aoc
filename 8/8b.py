orig = [(line.split()[0], int(line.split()[1])) for line in open("input")]

def run(prog):
    i = 0
    execd = set()
    acc = 0
    while i < len(prog) and i not in execd:
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
    if i >= len(prog):
        return acc
    else:
        return None

for j in range(len(orig)):
    if orig[j][0] == "nop":
        new = orig[:j] + [("jmp", orig[j][1])] + orig[j+1:]
    elif orig[j][0] == "acc":
        continue
    else:
        new = orig[:j] + [("nop", orig[j][1])] + orig[j+1:]
    a = run(new)
    if a is not None:
        print(a)
