inp = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

inp = [list("." + i + ".") for i in inp.split("\n") if i]
inp = [["."] * len(inp[0])] + inp + [["."] * len(inp[0])]
dirs = [[-1, 0], [-1, -1], [-1, 1], [0, -1], [0, 1], [1, 1], [1, 0], [1, -1]]
r = 0
lr = -1

while lr != r:
    lr = r
    for i in range(1, len(inp) - 1):
        for j in range(1, len(inp[0]) - 1):
            if inp[i][j] == "@":
                n = 0
                for a, b in dirs:
                    if inp[i+a][j+b] == "@":
                        n += 1
                if n < 4:
                    r += 1
                    inp[i][j] = "."

print(r)