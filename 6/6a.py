print(sum(len(set(c for x in g.split() for c in x)) for g in open("input").read().split("\n\n")))
