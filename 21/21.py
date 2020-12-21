from operator import itemgetter
from copy import copy

d = {}
all_ings = set()
lines = []
for line in open("input"):
    ingredients, allergens = line.split(" (contains ")
    ingredients = set(ingredients.split())
    all_ings |= ingredients
    allergens = allergens.rstrip("\n)").split(", ")
    lines.append((ingredients, allergens))
    for al in allergens:
        if al not in d:
            d[al] = copy(ingredients)
        else:
            d[al] &= ingredients

matching = {}
while True:
    remove_ing = set()
    remove_al = set()
    for al in d:
        if len(d[al]) == 1:
            ing = next(iter(d[al]))
            matching[al] = ing
            remove_ing.add(ing)
            remove_al.add(al)
    for al in remove_al:
        del d[al]
    for al in d:
        for ing in remove_ing:
            d[al].discard(ing)
    if not remove_ing and not remove_al:
        break

possible = set(matching.values()) | set.union(*d.values())
impossible = all_ings - possible
print(sum(1 for line in lines for ing in line[0] if ing in impossible))
print(",".join(x[1] for x in sorted(matching.items(), key=itemgetter(0))))
