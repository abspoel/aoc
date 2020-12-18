target = 1309761972
sums = []
for line in open("input"):
    x = int(line)
    sums = [y + x for y in sums + [0]]
    if target in sums:
        start = sums.index(target)
        length = len(sums) - sums.index(target)
        m1 = min(int(j) for j in open("input").readlines()[start:start+length])
        m2 = max(int(j) for j in open("input").readlines()[start:start+length])
        print(m1+m2)
        break
