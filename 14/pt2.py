inp = """
"""

xLen, yLen = 101, 103

inp = inp.split("\n")
inp = [i for i in inp if i]
inp = [i.replace("p=", "").split(" v=") for i in inp]
inp = [[list(map(int, a.split(","))), list(map(int, b.split(",")))] for a, b in inp]

pS = set()

s1, s2 = 0, 0
d1, d2 = 0, 0

for j in range(1, 20000):
    l = set()
    for i in range(len(inp)):
        inp[i][0][0] = (inp[i][0][0] + inp[i][1][0]) % xLen
        inp[i][0][1] = (inp[i][0][1] + inp[i][1][1]) % yLen
        l.add((inp[i][0][1], inp[i][0][0]))
    
    for a, b in l:
        s1 += a
        s2 += b
    s1 = s1 // len(l)
    s2 = s2 // len(l)
    for a, b in l:
        d1 += abs(s1-a)
        d2 += abs(s2-b)
    d1 = d1 // len(l)
    d2 = d2 // len(l)

    if d1 + d2 <= 30:
        for a in range(yLen):
            s = ""
            for b in range(xLen):
                if (a, b) in l:
                    s += "#"
                else:
                    s += " "
            print(s)
        print(j)
        break