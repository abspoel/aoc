import re
d = {}
for line in open("input"):
    container, contents = line.split(" bags contain ", maxsplit=1)
    l = []
    if not contents.startswith("no other bags"):
        for token in contents.split(", "):
            m = re.match("(\d+) (.+?) bag", token)
            l.append((int(m[1]), m[2]))
    d[container] = l

def contains(node):
    if not d[node]:
        return 0
    return sum(x[0]*(contains(x[1])+1) for x in d[node])

print(contains("shiny gold"))
