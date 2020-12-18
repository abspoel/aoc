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

visited = set()
def search(node):
    if node in visited:
        return
    visited.add(node)
    for k in d:
        if any(x[1] == node for x in d[k]):
            search(k)

search("shiny gold")
print(len(visited)-1) # could be off by 1
