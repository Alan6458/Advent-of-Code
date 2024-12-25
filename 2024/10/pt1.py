inp = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

inp = inp.split("\n")
inp = [i for i in inp if i]

h, z, t = {}, set(), set()
hn = {}
hOld = {}

for i in range(len(inp)):
    for j, v in enumerate(inp[i]):
        h[(i, j)] = set()
        hn[(i, j)] = set()
        hOld[(i, j)] = set()
        if v == "9":
            t.add((i, j))
        elif v == "0":
            z.add((i, j))
        for a, b in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if i+a >= 0 and i+a < len(inp) and j+b >= 0 and j+b < len(inp[i]):
                if int(inp[i+a][j+b]) - int(inp[i][j]) == 1:
                    h[(i, j)].add((i+a, j+b))

for i in range(100):
    for a, b in z:
        for c, d in h[(a, b)]:
            if (c, d) not in hOld[(a, b)]:
                for e, f in h[(c, d)]:
                    hn[(a, b)].add((e, f))
        hOld[(a, b)] = h[(a, b)].copy()
        for c, d in hn[(a, b)]:
            h[(a, b)].add((c, d))
        hn[(a, b)] = set()

r = 0
rOld = 0
for a, b in z:
    rOld = r
    for c, d in t:
        if (c, d) in h[(a, b)]:
            r += 1
print(r)