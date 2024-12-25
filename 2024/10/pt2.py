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

r = [0]

def recur(a, b, r):
    if (a, b) in t:
        r[0] += 1
        return
    for c, d in h[(a, b)]:
        recur(c, d, r)

for a, b in z:
    recur(a, b, r)
print(r[0])