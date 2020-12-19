from functools import lru_cache

rules = {}
rulepart, msgpart = open("input").read().split("\n\n")

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
        # Rule is tuple of tuple of ints, or str
        # Returns length of match
        if start >= len(msg):
            return 0
        if isinstance(rule, str):
            return 1 if msg[start] == rule else 0

        for choice in rule:
            i = start
            for num in choice:
                v = _match(i, rules[num])
                if v:
                    i += v
                else:
                    break
            else:
                return i - start
        return 0
    
    return _match(0, rules[0]) == len(msg)

print(sum(match(msg.strip()) for msg in msgpart.splitlines()))
