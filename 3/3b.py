from math import prod
print(prod(sum(line[a*i % (len(line)-1)] == "#" for i, line in enumerate(open("input").readlines()[::b])) for (a, b) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))
