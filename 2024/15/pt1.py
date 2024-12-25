inp = """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""

inp = inp.split("\n\n")
inp = [i for i in inp if i]
inp1 = inp[0]
inp2 = inp[1]
inp1 = inp1.split("\n")
inp1 = [i for i in inp1 if i]
inp2 = "".join(inp2).replace("\n", "")

lA, lB = len(inp1), len(inp1[0])
bCoords = set()
wCoords = set()
rA, rB = 0, 0
for i, v in enumerate(inp1):
    for j, c in enumerate(v):
        if c == "@":
            rA, rB = i, j
        elif c == "O":
            bCoords.add((i, j))
        elif c == "#":
            wCoords.add((i, j))

d = {">":[0, 1], "<":[0, -1], "v":[1, 0], "^":[-1, 0]}
for i in inp2:
    a, b = d[i][0], d[i][1]
    sA, sB = rA, rB
    canMove = False
    moveL = []
    while sA + a < lA and sA + a >= 0 and sB + b < lB and sB + b >= 0:
        sA, sB = sA+a, sB+b
        if (sA, sB) in wCoords:
            break
        elif (sA, sB) not in bCoords:
            canMove = True
            break
        bCoords.remove((sA, sB))
        moveL.append((sA, sB))
    if canMove:
        for aA, aB in moveL:
            bCoords.add((aA+a, aB+b))
        rA += a
        rB += b
    else:
        for aA, aB in moveL:
            bCoords.add((aA, aB))

r = 0
for a, b in bCoords:
    r += 100 * a + b
print(r)