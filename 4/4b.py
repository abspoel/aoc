import re
valid = {
    "byr": lambda x: x.isnumeric() and 1920 <= int(x) <= 2002,
    "iyr": lambda x: x.isnumeric() and 2010 <= int(x) <= 2020,
    "eyr": lambda x: x.isnumeric() and 2020 <= int(x) <= 2030,
    "hgt": lambda x: x[:-2].isnumeric() and (x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193)
                or (x[-2:] == "in" and 59 <= int(x[:-2]) <= 76),
    "hcl": lambda x: re.match(r"^\#[0-9a-f]{6}$", x),
    "ecl": lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
    "pid": lambda x: x.isnumeric() and len(x) == 9
}
cnt = 0
for pas in open("input").read().split("\n\n"):
    d = dict(x.split(":") for x in pas.split())
    cnt += all(k in d and valid[k](d[k]) for k in valid)
print(cnt)
