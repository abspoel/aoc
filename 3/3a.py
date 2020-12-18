print(sum(int(line[3*i % (len(line)-1)] == "#") for i, line in enumerate(open("input"))))
