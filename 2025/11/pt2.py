inp = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""

inp = [i.replace(":", "").split(" ") for i in inp.split("\n") if i]
inp.append(["out"])

r = 1

for a, b in [["svr", "fft"], ["fft", "dac"], ["dac", "out"]]:
    d = {i[0]:i[1:] for i in inp}
    d[b].append(b)
    d2 = {i[0]:0 for i in inp}
    d2[a] = 1
    for _ in range(10000):
        d2n = {i[0]:0 for i in inp}
        for i in d2:
            for j in d[i]:
                d2n[j] += d2[i]
        d2 = d2n
    r *= d2[b]

print(r)