def tokenize(line):
    token = []
    for ch in line:
        if ch.isnumeric():
            token.append(ch)
        elif token:
            yield int("".join(token))
            token = []
        if ch in "()+*":
            yield ch
    if token:
        yield int("".join(token))


def ev_tree(cur):
    i = 1
    while i < len(cur):
        if cur[i] == "+":
            cur = cur[:i-1] + [cur[i-1] + cur[i+1]] + cur[i+2:]
        else:
            i += 2
    i = 1
    while i < len(cur):
        if cur[i] == "*":
            cur = cur[:i-1] + [cur[i-1] * cur[i+1]] + cur[i+2:]
        else:
            i += 2
    return cur[0]


def ev(tokens):
    stack = []
    cur = []
    op = None

    for token in tokens:
        if token == "(":
            stack.append(cur)
            cur = []
        elif token == ")":
            result = ev_tree(cur)
            cur = stack.pop() + [result]
        else:
            cur.append(token)
    return ev_tree(cur)


print(sum(ev(tokenize(line)) for line in open("input")))
