from functools import lru_cache
from collections import defaultdict
j = [int(x) for x in open("input")]
j.sort()
print(list(enumerate(j)))

@lru_cache(maxsize=None)
def f(i):
    if i == len(j)-1:
        return 1
    if i == -1:
        ans = sum(f(k) for k in range(i+1, i+4) if k < len(j) and j[k] <= 3)
    else:
        ans = sum(f(k) for k in range(i+1, i+4) if k < len(j) and j[k] - j[i] <= 3)
    print((i, ans))
    return ans

print(f(-1))
