inp = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

inp = inp.split("\n")
inp = [i for i in inp if i]

dL = {}
for i, v in enumerate(inp):
    for j, c in enumerate(v):
        if c == ".":
            continue
        if c not in dL:
            dL[c] = []
        dL[c].append((i, j))

s = set()

r = 0

inpA = len(inp)
inpB = len(inp[0])
for i in dL:
    for j, (a, b) in enumerate(dL[i]):
        for c, d in dL[i][j+1:]:
            if a >= c and b >= d:
                m = 0
                while a+m*abs(c-a) < inpA and b+m*abs(d-b) < inpB:
                    s.add((a+m*abs(c-a), b+m*abs(d-b)))
                    m += 1
                m = 0
                while c-m*abs(c-a) >= 0 and d-m*abs(d-b) >= 0:
                    s.add((c-m*abs(c-a), d-m*abs(d-b)))
                    m += 1
            elif a <= c and b <= d:
                m = 0
                while a-m*abs(c-a) >= 0 and b-m*abs(d-b) >= 0:
                    s.add((a-m*abs(c-a), b-m*abs(d-b)))
                    m += 1
                m = 0
                while c+m*abs(c-a) < inpA and d+m*abs(d-b) < inpB:
                    s.add((c+m*abs(c-a), d+m*abs(d-b)))
                    m += 1
            elif a >= c and b <= d:
                m = 0
                while a+m*abs(c-a) < inpA and b-m*abs(d-b) >= 0:
                    s.add((a+m*abs(c-a), b-m*abs(d-b)))
                    m += 1
                m = 0
                while c-m*abs(c-a) >= 0 and d+m*abs(d-b) < inpB:
                    s.add((c-m*abs(c-a), d+m*abs(d-b)))
                    m += 1
            else:
                m = 0
                while a-m*abs(c-a) >= 0 and b+m*abs(d-b) < inpB:
                    s.add((a-m*abs(c-a), b+m*abs(d-b)))
                    m += 1
                m = 0
                while c+m*abs(c-a) < inpA and d-m*abs(d-b) >= 0:
                    s.add((c+m*abs(c-a), d-m*abs(d-b)))
                    m += 1

for a, b in s:
    if 0 <= a and a < inpA and 0 <= b and b < inpB:
        r += 1
print(r)