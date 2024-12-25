inp = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""

import sys
sys.setrecursionlimit(1000000)

inp = inp.split("\n")
inp = [i for i in inp if i]

inpA, inpB = len(inp), len(inp[0])
w = set()

sa, sb, ea, eb = 0, 0, 0, 0

for a in range(len(inp)):
    for b in range(len(inp[a])):
        if inp[a][b] == "#":
            w.add((a, b))
        elif inp[a][b] == "S":
            sa, sb = a, b
        elif inp[a][b] == "E":
            ea, eb = a, b

vlm = [100000000]

v = [[100000000] * inpB for _ in range(inpA)]

def t(w, inpA, inpB, a, b, ea, eb, v, vlm, cs):
    if cs > vlm[0]:
        return
    if cs > v[a][b]:
        return
    v[a][b] = cs
    if a == ea and b == eb:
        if vlm[0] > cs:
            vlm[0] = cs
        return
    for an, bn in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if a + an >= 0 and a + an < inpA and b + bn >= 0 and b + bn < inpB:
            if (a+an, b+bn) not in w:
                t(w, inpA, inpB, a+an, b+bn, ea, eb, v, vlm, cs+1)
t(w, inpA, inpB, sa, sb, ea, eb, v, vlm, 0)

r = 0
for a in range(1, len(inp)-1):
    for b in range(1, len(inp[a])-1):
        if inp[a-1][b] != "#" and inp[a+1][b] != "#":
            if abs(v[a-1][b]-v[a+1][b])-2 >= 100 and v[a-1][b] != 100000000 and v[a+1][b] != 100000000:
                r += 1
        elif inp[a][b-1] != "#" and inp[a][b+1] != "#":
            if abs(v[a][b-1]-v[a][b+1])-2 >= 100 and v[a][b-1] != 100000000 and v[a][b+1] != 100000000:
                r += 1

print(r)