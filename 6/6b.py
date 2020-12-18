from functools import reduce
print(sum(len(reduce(set.intersection, (set(x) for x in g.split()))) for g in open("input").read().split("\n\n")))
