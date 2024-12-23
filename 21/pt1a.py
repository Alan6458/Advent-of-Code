inp = """
029A
980A
179A
456A
379A
"""

inp = inp.split("\n")
inp = [i for i in inp if i]

d = {"0":(1, 3), "1":(0, 2), "2":(1, 2), "3":(2, 2), "4":(0, 1), "5":(1, 1), "6":(2, 1), "7":(0, 0), "8":(1, 0), "9":(2, 0), "A":(2, 3)}
d1 = {"^":(1, 0), "<":(0, 1), "v":(1, 1), ">":(2, 1), "A":(2, 0)}

def mr(x, y, cs, gs, ci, fs, d1, v, nx, ny):
    if x == nx and y == ny:
        return
    if ci == len(gs):
        fs.add(cs)
        return
    if (cs, x, y, ci) not in v:
        v.add((cs, x, y))
    else:
        return
    if y > d1[gs[ci]][1]:
        mr(x, y-1, cs + "^", gs, ci, fs, d1, v, nx, ny)
    if x < d1[gs[ci]][0]:
        mr(x+1, y, cs + ">", gs, ci, fs, d1, v, nx, ny)
    if y < d1[gs[ci]][1]:
        mr(x, y+1, cs + "v", gs, ci, fs, d1, v, nx, ny)
    if x > d1[gs[ci]][0]:
        mr(x-1, y, cs + "<", gs, ci, fs, d1, v, nx, ny)
    if x == d1[gs[ci]][0] and y == d1[gs[ci]][1]:
        mr(x, y, cs + "A", gs, ci + 1, fs, d1, v, nx, ny)

cPos = [[2, 3], [2, 0], [2, 0]]
r = 0
for i in inp:
    v = set()
    fs = set()
    mr(2, 3, "", i, 0, fs, d, v, 0, 3)
    v = set()
    fs1 = set()
    for j in fs:
        mr(2, 0, "", j, 0, fs1, d1, v, 0, 0)
    v = set()
    fs2 = set()
    for j in fs1:
        mr(2, 0, "", j, 0, fs2, d1, v, 0, 0)
    f = "-" * 1000
    for j in fs2:
        if len(j) < len(f):
            f = j
    r += int(i[:3]) * len(f)
print(r)