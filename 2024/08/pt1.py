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

# I somehow copied my input wrong on part 1

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

inpA = len(inp)
inpB = len(inp[0])
for i in dL:
    for j, (a, b) in enumerate(dL[i]):
        for c, d in dL[i][j+1:]:
            if a >= c and b >= d:
                s.add((a+abs(c-a), b+abs(d-b)))
                s.add((c-abs(c-a), d-abs(d-b)))
            elif a <= c and b <= d:
                s.add((a-abs(c-a), b-abs(d-b)))
                s.add((c+abs(c-a), d+abs(d-b)))
            elif a >= c and b <= d:
                s.add((a+abs(c-a), b-abs(d-b)))
                s.add((c-abs(c-a), d+abs(d-b)))
            else:
                s.add((a-abs(c-a), b+abs(d-b)))
                s.add((c+abs(c-a), d-abs(d-b)))

r = 0
for a, b in s:
    if 0 <= a and a < inpA and 0 <= b and b < inpB:
        r += 1
print(r)