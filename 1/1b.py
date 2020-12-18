def solve():
    lst = list(sorted(map(int, open("input").readlines())))
    t = [(a, b, c) for a in lst for b in lst for c in lst if a + b + c == 2020][0]
    return t[0]*t[1]*t[2]

print(solve())
