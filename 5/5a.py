print(max(int(x.translate(str.maketrans("FBLR", "0101")), 2) for x in open("input")))
