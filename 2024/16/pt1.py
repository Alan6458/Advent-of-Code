inp = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""

# first time importing stuff
import sys
sys.setrecursionlimit(100000)

inp = inp.split("\n")
inp = [i for i in inp if i]

ga, gb = 1, len(inp[0])-2
a, b = len(inp)-2, 1
v = [[100000000 for b in range(len(inp[a]))] for a in range(len(inp))]
def t(inp, a, b, da, db, cs, v, ga, gb):
    if a == ga and b == gb:
        if v[a][b] > cs:
            v[a][b] = cs
        return
    if v[a][b] < cs:
        return
    v[a][b] = cs
    for na, nb in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        if inp[a+na][b+nb] != "#":
            if na == da and nb == db:
                t(inp, a+na, b+nb, na, nb, cs+1, v, ga, gb)
            else:
                t(inp, a+na, b+nb, na, nb, cs+1001, v, ga, gb)

t(inp, a, b, 0, 1, 0, v, ga, gb)
print(v[ga][gb])