def solve():
    lst = list(sorted(map(int, open("input").readlines())))
    fwd, rev = iter(lst), iter(reversed(lst))
    a = next(fwd)
    b = next(rev)
    target = 2020
    while True:
        print((a, b, a+b))
        if a + b < target:
            a = next(fwd)
        elif a + b > target:
            b = next(rev)
        else:
            return a*b

print(solve())
