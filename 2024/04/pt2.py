inp = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

inp = inp.split("\n")
inp = [i for i in inp if i != ""]

r = 0
l = [[[1, 1], [-1, -1]], [[-1, -1], [1, 1]], [[-1, 1], [1, -1]], [[1, -1], [-1, 1]]]
xmas = "MS"
ct = 0

for i in range(1, len(inp)-1):
    for j in range(1, len(inp[i])-1):
        ct = 0
        for c in range(len(l)):
            if all(inp[i+a][j+b] == xmas[k] for k, [a, b] in enumerate(l[c])) and inp[i][j] == "A":
                ct += 1
        if ct == 2:
            r += 1
print(r)