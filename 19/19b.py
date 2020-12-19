rules = {}

rulepart, msgpart = open("input2").read().split("\n\n")

for line in rulepart.splitlines():
    num, rule = line.split(":")
    num = int(num.strip())
    rule = rule.strip()
    if rule.startswith('"'):
        rules[num] = rule[1]
    else:
        subrules = rule.strip().split("|")
        rules[num] = tuple(tuple(int(x) for x in sub.strip().split()) for sub in subrules)

def match(msg):
    def _match(start, rule):
        # Rule is tuple of tuples of ints, or str
        # Returns set of final indices
        if start >= len(msg):
            return
        if isinstance(rule, str):
            return set([start+1]) if msg[start] == rule else None

        my_ends = set()
        for choice in rule:
            ixs = set([start])
            for num in choice:
                next_ixs = set()
                for i in ixs:
                    ends = _match(i, rules[num])
                    if ends:
                        next_ixs |= set(ends)
                if not next_ixs:
                    break
                ixs = next_ixs
            else:
                my_ends |= ixs
        return my_ends if my_ends else None
    
    v = _match(0, rules[0])
    return v is not None and len(msg) in v

print(sum(match(msg.strip()) for msg in msgpart.splitlines()))
