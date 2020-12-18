import re
cnt = 0
for line in open("input"):
    m = re.match("(\d+)-(\d+) (\w): (\S+)", line)
    if int(m[1]) <= m[4].count(m[3]) <= int(m[2]):
        cnt += 1
print(cnt)
