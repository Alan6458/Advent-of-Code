inp = """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""

inp = inp.split("\n")
inp = [i for i in inp if i]
inp = [i.split("-") for i in inp]

d = {}
for a, b in inp:
    if a not in d:
        d[a] = set()
    if b not in d:
        d[b] = set()
    d[a].add(b)
    d[b].add(a)

r = set()
for i in d:
    if i[0] != "t":
        continue
    for j in d[i]:
        for k in d[j]:
            if k in d[i]:
                t = sorted([i, j, k])
                if (t[0], t[1], t[2]) not in r:
                    r.add((t[0], t[1], t[2]))
print(len(r))