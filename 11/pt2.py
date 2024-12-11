inp = "125 17"

inp = inp.split(" ")

nextD = {"0":["1"]}

d = {}
dNew = {}
for i in inp:
    if i not in d:
        d[i] = 0
    d[i] += 1

for i in range(75):
    for j in d:
        if j not in nextD:
            if len(j) % 2 == 0:
                nextD[j] = [j[:len(j)//2], str(int(j[len(j)//2:]))]
            else:
                nextD[j] = [str(int(j)*2024)]
        for k in nextD[j]:
            if k not in dNew:
                dNew[k] = 0
            dNew[k] += d[j]
    for j in d:
        d[j] = 0
    for j in dNew:
        d[j] = dNew[j]
        dNew[j] = 0
print(sum(d.values()))