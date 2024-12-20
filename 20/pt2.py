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

v = [[100000000] * inpB for _ in range(inpA)]

def t(w, inpA, inpB, a, b, ea, eb, v, cs):
    if cs > v[a][b]:
        return
    v[a][b] = cs
    if a == ea and b == eb:
        return
    for an, bn in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if a + an >= 0 and a + an < inpA and b + bn >= 0 and b + bn < inpB:
            if (a+an, b+bn) not in w:
                t(w, inpA, inpB, a+an, b+bn, ea, eb, v, cs+1)

t(w, inpA, inpB, sa, sb, ea, eb, v, 0)

pl = {}
for a in range(inpA):
    for b in range(inpB):
        if v[a][b] != 100000000:
            pl[(a, b)] = v[a][b]

# Why did I use recursion? Because I misread instructons for pt2...
# I thought "same cheat" meant I couldn't go into normal track
# Wasted like three and a half hours on this

def wr(w, a, b, v, on, nl, av, pl):
    if nl == 20:
        return
    if (a, b) not in v:
        v[(a, b)] = nl
    elif v[(a, b)] > nl:
        v[(a, b)] = nl
    else:
        return
    for an, bn in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        wr(w, a+an, b+bn, v, on, nl+1, av, pl)
        # Make sure to change the next line!
        if (a+an, b+bn) in pl and pl[(a+an, b+bn)] - on - nl - 1 >= 100:
            av.add((on, pl[(a+an, b+bn)]))

av = set()
for a, b in pl:
    v = {}
    wr(w, a, b, v, pl[(a, b)], 0, av, pl)
print(len(av))