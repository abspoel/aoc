print(sum(set(x.split(":")[0] for x in pas.split()) >= {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
       for pas in open("input").read().split("\n\n")))
