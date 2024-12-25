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

# This was the first brute-force solution that took an actually noticeable amount of time

inp = inp.split("\n")
inp = [list(i) for i in inp if i != ""]

a, b = 0, 0
for i, v in enumerate(inp):
    if "^" in v:
        a = i
        b = v.index("^")
        break
inp[a][b] = "."
aOrig, bOrig = a, b

dirL = [[-1, 0], [0, 1], [1, 0], [0, -1]]
dir = 0
r = 0

for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j] == "#":
            continue
        inp[i][j] = "#"
        visited = set()
        a, b = aOrig, bOrig
        dir = 0
        while 0 <= a and a < len(inp) and 0 <= b and b < len(inp[0]):
            if (a, b, dir) not in visited:
                visited.add((a, b, dir))
            else:
                r += 1
                break
            if (dir == 0 and a == 0) or (dir == 1 and b == len(inp[0])-1) or (dir == 2 and a == len(inp)-1) or (dir == 3 and b == 0):
                break
            if inp[a+dirL[dir][0]][b+dirL[dir][1]] == "#":
                dir = (dir + 1) % 4
            else:
                a += dirL[dir][0]
                b += dirL[dir][1]
        inp[i][j] = "."

print(r)