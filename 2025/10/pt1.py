inp = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

inp = [i.split(" ") for i in inp.split("\n") if i]
bG = [i[0] for i in inp]
bG = [list(i[1:-1]) for i in bG]
inp = [i[1:-1] for i in inp]
inp = [[list(map(int, j[1:-1].split(","))) for j in i] for i in inp]

r = 0
for i in range(len(inp)):
    m = 10000
    for j in range(2 ** len(inp[i])):
        b = list(bin(j)[2:].zfill(len(inp[i])))
        cs = [False for k in range(len(bG[i]))]
        for k in range(len(b)):
            if b[k] == "1":
                for l in inp[i][k]:
                    cs[l] = not cs[l]
        cs = ["#" if i else "." for i in cs]
        if all(bG[i][k] == cs[k] for k in range(len(cs))):
            if b.count("1") < m:
                m = b.count("1")
    r += m
print(r)