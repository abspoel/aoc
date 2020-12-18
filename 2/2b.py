import re
cnt = 0
for line in open("input"):
    m = re.match("(\d+)-(\d+) (\w): (\S+)", line)
    if int(m[4][int(m[1])-1] == m[3]) + int(m[4][int(m[2])-1] == m[3]) == 1:
        cnt += 1
print(cnt)
