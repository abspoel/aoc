from collections import defaultdict
j = [int(x) for x in open("input")]
j.sort()
prev = 0
diff = defaultdict(lambda: 0)
for x in j:
    diff[x - prev] += 1
    prev = x
diff[3] += 1
print(diff[1]*diff[3])
