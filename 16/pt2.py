inp = """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""

# I had to COMPLETELY RESTART p2 after AN HOUR OF WORKING ON IT

import sys
sys.setrecursionlimit(100000)

inp = inp.split("\n")
inp = [i for i in inp if i]

pt1ans = int(input("What is pt1 solution???:"))

ga, gb = 1, len(inp[0])-2
a, b = len(inp)-2, 1
v = [[pt1ans for b in range(len(inp[a]))] for a in range(len(inp))]
p = set()
fp = set()
def t(inp, a, b, da, db, cs, v, ga, gb, p, fp):
    p.add((a, b))
    if a == ga and b == gb:
        if v[a][b] == cs:
            for i in p:
                fp.add(i)
        return
    # I added the + 2000 on the next line and it somehow started working... wtffffff
    # I swear it's an actual miracle
    if cs > v[a][b] and cs != v[a][b] + 1000 and cs != v[a][b] + 2000:
        return
    v[a][b] = cs
    for na, nb in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        if inp[a+na][b+nb] != "#":
            if na == da and nb == db:
                t(inp, a+na, b+nb, na, nb, cs+1, v, ga, gb, p.copy(), fp)
            else:
                t(inp, a+na, b+nb, na, nb, cs+1001, v, ga, gb, p.copy(), fp)

t(inp, a, b, 0, 1, 0, v, ga, gb, p, fp)
print(len(fp))