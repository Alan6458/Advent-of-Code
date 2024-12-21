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

cPos = [[2, 3], [2, 0], [2, 0]]
r = 0
for i in inp:
    cr = 0
    s1 = ""
    s2 = ""
    s3 = ""
    for j in i:
        if not (cPos[0][1] == 3 and d[j][0] == 0):
            while cPos[0][0] > d[j][0]:
                s1 += "<"
                cPos[0][0] -= 1
        if not (cPos[0][0] == 0 and d[j][1] == 3):
            while cPos[0][1] < d[j][1]:
                s1 += "v"
                cPos[0][1] += 1
        while cPos[0][0] < d[j][0]:
            s1 += ">"
            cPos[0][0] += 1
        while cPos[0][1] > d[j][1]:
            s1 += "^"
            cPos[0][1] -= 1
        while cPos[0][0] > d[j][0]:
            s1 += "<"
            cPos[0][0] -= 1
        while cPos[0][1] < d[j][1]:
            s1 += "v"
            cPos[0][1] += 1
        s1 += "A"
    for k in s1:
        if cPos[1][0] != 0:
            while cPos[1][1] > d1[k][1]:
                s2 += "^"
                cPos[1][1] -= 1
        while cPos[1][0] < d1[k][0]:
            s2 += ">"
            cPos[1][0] += 1
        while cPos[1][1] > d1[k][1]:
            s2 += "^"
            cPos[1][1] -= 1
        while cPos[1][1] < d1[k][1]:
            s2 += "v"
            cPos[1][1] += 1
        while cPos[1][0] > d1[k][0]:
            s2 += "<"
            cPos[1][0] -= 1
        s2 += "A"
    for k in s2:
        if cPos[2][0] != 0:
            while cPos[2][1] > d1[k][1]:
                s3 += "^"
                cPos[2][1] -= 1
        while cPos[2][0] < d1[k][0]:
            s3 += ">"
            cPos[2][0] += 1
        while cPos[2][1] > d1[k][1]:
            s3 += "^"
            cPos[2][1] -= 1
        while cPos[2][1] < d1[k][1]:
            s3 += "v"
            cPos[2][1] += 1
        while cPos[2][0] > d1[k][0]:
            s3 += "<"
            cPos[2][0] -= 1
        s3 += "A"
    r += int(i[:3]) * len(s3)
print(r)