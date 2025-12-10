inp = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

import scipy

inp = [i.split(" ") for i in inp.split("\n") if i]
jr = [i[-1] for i in inp]
jr = [list(map(int, i[1:-1].split(","))) for i in jr]
inp = [i[1:-1] for i in inp]
inp = [[list(map(int, j[1:-1].split(","))) for j in i] for i in inp]

r = 0
for i in range(len(inp)):
    na = [[1 if j in inp[i][k] else 0 for k in range(len(inp[i]))] for j in range(len(jr[i]))]
    rb = scipy.optimize.linprog(c = [1] * len(na[0]), A_eq = na, b_eq = jr[i], integrality = 1)
    r += rb.fun

print(round(r))