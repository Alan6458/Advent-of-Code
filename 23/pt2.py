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

# Actually easy after experiencing the absolute nightmare of day 21
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

nl = [set([i]) for i in d]
cn = 0
for i in d:
    for j in range(len(nl)):
        a = True
        for k in nl[j]:
            if k not in d[i]:
                a = False
                break
        if a:
            nl.append(nl[j].copy())
            nl[j].add(i)
    # Code not working? Try shuffling order of the dictionary keys
    while len(nl) > 5000:
        nl.pop(-1)
    cn += 1
l = set()
for i in nl:
    if len(i) > len(l):
        l = i
print(",".join(sorted(list(l))))