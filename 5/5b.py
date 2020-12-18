s = {int(x.translate(str.maketrans("FBLR", "0101")), 2) for x in open("input")}
print(set(range(min(s), max(s)+1)) - s)
