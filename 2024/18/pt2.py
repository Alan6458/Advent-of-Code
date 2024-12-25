inp = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""

import sys
sys.setrecursionlimit(100000)

# CONFIGURE:
areaLength = 7

inp = inp.split("\n")
inp = [i for i in inp if i]
inp = [list(map(int, i.split(",")))[::-1] for i in inp]

m = set()

def t(v, m, a, b, s, vl, fvl):
    if s >= v[a][b]:
        return
    if s >= v[-1][-1]:
        return
    if len(vl) > len(fvl[0]):
        return
    vl.add((a, b))
    v[a][b] = s
    if a == len(v)-1 and b == len(v)-1:
        if v[a][b] == s:
            fvl[0] = vl
        return
    for ap, bp in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        if a + ap < len(v) and a + ap >= 0 and b + bp < len(v) and b + bp >= 0:
            if (a+ap, b+bp) not in m:
                t(v, m, a+ap, b+bp, s+1, vl.copy(), fvl)

fvl = [set(range(10000))]
v = [[100000000] * areaLength for _ in range(areaLength)]
t(v, m, 0, 0, 0, set(), fvl)
ind = 0
for a, b in inp:
    m.add((a, b))
    if (a, b) in fvl[0]:
        v = [[100000000] * areaLength for _ in range(areaLength)]
        fvl = [set(range(10000))]
        t(v, m, 0, 0, 0, set(), fvl)
        if v[areaLength-1][areaLength-1] == 100000000:
            print(str(b) + "," + str(a))
            break
    ind += 1