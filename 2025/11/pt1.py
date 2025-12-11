inp = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

inp = [i.replace(":", "").split(" ") for i in inp.split("\n") if i]
inp.append(["out", "out"])

d = {i[0]:i[1:] for i in inp}

d2 = {i[0]:0 for i in inp}
d2["you"] = 1

for _ in range(10000):
    d2n = {i[0]:0 for i in inp}
    for i in d2:
        for j in d[i]:
            d2n[j] += d2[i]
    d2 = d2n

print(d2["out"])