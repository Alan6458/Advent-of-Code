inp = """
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""

inp = inp.split("\n\n")
inp = [i for i in inp if i]
inp = [i.split("\n") for i in inp]
inp = [[j for j in i if j] for i in inp]

locks = []
keys = []
for i in inp:
    if i[0] == "#####":
        locks.append((len([j for j in i if j[0] == "#"]), len([j for j in i if j[1] == "#"]), len([j for j in i if j[2] == "#"]), len([j for j in i if j[3] == "#"]), len([j for j in i if j[4] == "#"])))
    if i[6] == "#####":
        keys.append((7-len([j for j in i if j[0] == "#"]), 7-len([j for j in i if j[1] == "#"]), 7-len([j for j in i if j[2] == "#"]), 7-len([j for j in i if j[3] == "#"]), 7-len([j for j in i if j[4] == "#"])))

r = 0
for a, b, c, d, e in keys:
    for f, g, h, i, j in locks:
        if a >= f and b >= g and c >= h and d >= i and e >= j:
            r += 1
print(r)