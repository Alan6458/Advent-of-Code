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
processLen = 12

inp = inp.split("\n")
inp = [i for i in inp if i]
inp = [list(map(int, i.split(",")))[::-1] for i in inp]

m = [["." for _ in range(areaLength)] for _ in range(areaLength)]

for i in range(processLen):
    m[inp[i][0]][inp[i][1]] = "#"

v = [[100000000] * areaLength for _ in range(areaLength)]
def t(v, m, a, b, s):
    if v[a][b] <= s:
        return
    v[a][b] = s
    if a == len(v)-1 and b == len(v)-1:
        return
    for ap, bp in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if a + ap < len(v) and a + ap >= 0 and b + bp < len(v) and b + bp >= 0:
            if m[a+ap][b+bp] != "#":
                t(v, m, a+ap, b+bp, s+1)
t(v, m, 0, 0, 0)
print(v[areaLength-1][areaLength-1])