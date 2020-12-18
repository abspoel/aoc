buf = []
for line in open("input"):
    x = int(line)
    if len(buf) < 25:
        buf.append(x)
    else:
        print(buf)
        for y in buf:
            if x - y in buf:
                break
        else:
            break
        buf.pop(0)
        buf.append(x)
        
print(x)
