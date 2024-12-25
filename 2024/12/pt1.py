inp = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

inp = inp.split("\n")
inp = [i for i in inp if i]

v = set()

def t(a, b, l, v, inp):
    v.add((a, b))
    l[0] += 1
    for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if a+i >= 0 and a+i < len(inp) and b+j >= 0 and b+j < len(inp[0]):
            if (a+i, b+j) not in v:
                if inp[a+i][b+j] == inp[a][b]:
                    t(a+i, b+j, l, v, inp)
            if inp[a+i][b+j] != inp[a][b]:
                l[1] += 1
        else:
            l[1] += 1

r = 0
for i in range(len(inp)):
    for j in range(len(inp[0])):
        if (i, j) not in v:
            l = [0, 0]
            t(i, j, l, v, inp)
            r += l[0] * l[1]
            # print(l, l[0] * l[1], inp[i][j])
print(r)