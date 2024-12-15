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

inp = inp.replace(".", "..").replace("#", "##").replace("O", "[]").replace("@", "@.")
inp = inp.split("\n\n")
inp = [i for i in inp if i]
inp1 = inp[0]
inp2 = inp[1]
inp1 = inp1.split("\n")
inp1 = [i for i in inp1 if i]
inp2 = "".join(inp2).replace("\n", "")

lA, lB = len(inp1), len(inp1[0])
bCoords1 = set()
bCoords2 = set()
wCoords = set()
rA, rB = 0, 0
for i, v in enumerate(inp1):
    for j, c in enumerate(v):
        if c == "@":
            rA, rB = i, j
        elif c == "[":
            bCoords1.add((i, j))
        elif c == "]":
            bCoords2.add((i, j))
        elif c == "#":
            wCoords.add((i, j))

d = {">":[0, 1], "<":[0, -1], "v":[1, 0], "^":[-1, 0]}
for i in inp2:
    a, b = d[i][0], d[i][1]
    sA, sB = rA, rB
    canMove = False
    moveL1 = []
    moveL2 = []
    if b:
        while sA + a < lA and sA + a >= 0 and sB + b < lB and sB + b >= 0:
            sA, sB = sA+a, sB+b
            if (sA, sB) in wCoords:
                break
            elif (sA, sB) not in bCoords1 and (sA, sB) not in bCoords2:
                canMove = True
                break
            if (sA, sB) in bCoords1:
                bCoords1.remove((sA, sB))
                moveL1.append((sA, sB))
            else:
                bCoords2.remove((sA, sB))
                moveL2.append((sA, sB))
    else:
        sB = set([rB])
        while sA + a < lA and sA + a >= 0:
            sBNew = set()
            sA = sA+a
            if any((sA, j) in wCoords for j in sB):
                break
            elif all((sA, j) not in bCoords1 and (sA, j) not in bCoords2 for j in sB):
                canMove = True
                break
            for j in sB:
                if (sA, j) in bCoords1:
                    bCoords1.remove((sA, j))
                    moveL1.append((sA, j))
                    bCoords2.remove((sA, j+1))
                    moveL2.append((sA, j+1))
                    sBNew.add(j+1)
                    sBNew.add(j)
                elif (sA, j) in bCoords2:
                    bCoords2.remove((sA, j))
                    moveL2.append((sA, j))
                    bCoords1.remove((sA, j-1))
                    moveL1.append((sA, j-1))
                    sBNew.add(j-1)
                    sBNew.add(j)
            sB = sBNew.copy()
    if canMove:
        for aA, aB in moveL1:
            bCoords1.add((aA+a, aB+b))
        for aA, aB in moveL2:
            bCoords2.add((aA+a, aB+b))
        rA += a
        rB += b
    else:
        for aA, aB in moveL1:
            bCoords1.add((aA, aB))
        for aA, aB in moveL2:
            bCoords2.add((aA, aB))
    # for k in range(lA):
    #     s = ""
    #     for l in range(lB):
    #         if (k, l) in wCoords:
    #             s += "#"
    #         elif (k, l) in bCoords1:
    #             s += "["
    #         elif (k, l) in bCoords2:
    #             s += "]"
    #         elif k == rA and l == rB:
    #             s += "@"
    #         else:
    #             s += "."
    #     print(s)

r = 0
for a, b in bCoords1:
    r += 100 * a + b
print(r)