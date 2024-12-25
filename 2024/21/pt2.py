inp = """
029A
980A
179A
456A
379A
"""

inp = inp.split("\n")
inp = [i for i in inp if i]

d = {"0":(1, 3), "1":(0, 2), "2":(1, 2), "3":(2, 2), "4":(0, 1), "5":(1, 1), "6":(2, 1), "7":(0, 0), "8":(1, 0), "9":(2, 0), "A":(2, 3)}
d1 = {"^":(1, 0), "<":(0, 1), "v":(1, 1), ">":(2, 1), "A":(2, 0)}

d2 = {i+j:[] for i in "A^>v<" for j in "A^>v<"}
for i in d2:
    cPos = [[], [d1[i[0]][0], d1[i[0]][1]]]
    s2n = "A"
    if not ((cPos[1][0] == 1 and cPos[1][1] == 0) or (cPos[1][0] == 2 and cPos[1][1] == 0 and i[1] == "<")):
        while cPos[1][0] > d1[i[1]][0]:
            s2n += "<"
            cPos[1][0] -= 1
    while cPos[1][1] < d1[i[1]][1]:
        s2n += "v"
        cPos[1][1] += 1
    if cPos[1][0] != 0:
        while cPos[1][1] > d1[i[1]][1]:
            s2n += "^"
            cPos[1][1] -= 1
    while cPos[1][0] < d1[i[1]][0]:
        s2n += ">"
        cPos[1][0] += 1
    while cPos[1][1] > d1[i[1]][1]:
        s2n += "^"
        cPos[1][1] -= 1
    while cPos[1][0] > d1[i[1]][0]:
        s2n += "<"
        cPos[1][0] -= 1
    s2n += "A"
    for j in range(len(s2n)-1):
        d2[i].append(s2n[j:j+2])
cPos = [[2, 3], [2, 0], [2, 0]]
r = 0
for i in inp:
    rd = {i:0 for i in d2}
    rdt = {i:0 for i in d2}
    s1 = ""
    s2 = ""
    s2n = ""
    for j in i:
        if not (cPos[0][1] == 3 and d[j][0] == 0):
            while cPos[0][0] > d[j][0]:
                s1 += "<"
                cPos[0][0] -= 1
        if not (cPos[0][0] == 0 and d[j][1] == 3):
            while cPos[0][1] < d[j][1]:
                s1 += "v"
                cPos[0][1] += 1
        while cPos[0][1] > d[j][1]:
            s1 += "^"
            cPos[0][1] -= 1
        while cPos[0][0] < d[j][0]:
            s1 += ">"
            cPos[0][0] += 1
        while cPos[0][0] > d[j][0]:
            s1 += "<"
            cPos[0][0] -= 1
        while cPos[0][1] < d[j][1]:
            s1 += "v"
            cPos[0][1] += 1
        s1 += "A"
    s2 = s1
    s2 = "A" + s2
    for j in range(len(s2)-1):
        rd[s2[j:j+2]] += 1
    for l in range(25):
        for j in rd:
            for k in d2[j]:
                rdt[k] += rd[j]
        rd = rdt
        rdt = {i:0 for i in d2}
    r += int(i[:3]) * sum(rd.values())
print(r)