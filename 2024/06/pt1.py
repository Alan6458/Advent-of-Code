inp = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

inp = inp.split("\n")
inp = [list(i) for i in inp if i != ""]

a, b = 0, 0
for i, v in enumerate(inp):
    if "^" in v:
        a = i
        b = v.index("^")
        break
inp[a][b] = "."

visited = set()

dirL = [[-1, 0], [0, 1], [1, 0], [0, -1]]
dir = 0

while 0 <= a and a < len(inp) and 0 <= b and b < len(inp[0]):
    if (a, b) not in visited:
        visited.add((a, b))
    if (dir == 0 and a == 0) or (dir == 1 and b == len(inp[0])-1) or (dir == 2 and a == len(inp)-1) or (dir == 3 and b == 0):
        break
    if inp[a+dirL[dir][0]][b+dirL[dir][1]] == "#":
        dir = (dir + 1) % 4
    else:
        a += dirL[dir][0]
        b += dirL[dir][1]
print(len(visited))