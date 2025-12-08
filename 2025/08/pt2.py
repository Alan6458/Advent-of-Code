inp = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

inp = [i.split(",") for i in inp.split("\n") if i]
inp = [(int(a), int(b), int(c)) for a, b, c in inp]

l = []

for i in range(len(inp) - 1):
    for j in range(i + 1, len(inp)):
        l.append([((inp[i][0] - inp[j][0]) ** 2 + (inp[i][1] - inp[j][1]) ** 2 + (inp[i][2] - inp[j][2]) ** 2) ** 0.5, i, j])

l = sorted(l)

sl = [set([i]) for i in range(len(inp))]
d = {i:i for i in range(len(inp))}

nl = len(inp)

for ind in range(len(l)):
    i, j = l[ind][1], l[ind][2]
    fi = d[j]
    if fi == d[i]:
        continue
    for k in sl[d[j]]:
        d[k] = d[i]
    sl[d[i]] = sl[d[i]].union(sl[fi])
    sl[fi] = set()
    nl -= 1
    if nl == 1:
        print(inp[i][0] * inp[j][0])
        break