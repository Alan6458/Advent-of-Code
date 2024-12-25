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
l = [[[0, 0], [1, 0], [2, 0], [3, 0]], [[0, 0], [-1, 0], [-2, 0], [-3, 0]], [[0, 0], [0, 1], [0, 2], [0, 3]], [[0, 0], [0, -1], [0, -2], [0, -3]], [[0, 0], [1, 1], [2, 2], [3, 3]], [[0, 0], [-1, -1], [-2, -2], [-3, -3]], [[0, 0], [1, -1], [2, -2], [3, -3]], [[0, 0], [-1, 1], [-2, 2], [-3, 3]]]
xmas = "XMAS"

for i in range(len(inp)):
    for j in range(len(inp[i])):
        for c in range(len(l)):
            try:
                if all(inp[i+a][j+b] == xmas[k] for k, [a, b] in enumerate(l[c])) and i + l[c][3][0] >= 0  and j + l[c][3][1] >= 0:
                    r += 1
            except:
                pass
print(r)