inp = """
1
2
3
2024
"""

inp = inp.split("\n")
inp = [i for i in inp if i]
inp = list(map(int, inp))

d = {}
for i, c in enumerate(inp):
    v = set()
    s = []
    n = c
    for j in range(2000):
        pn = int(str(n)[-1])
        n = (n ^ (n * 64)) % 16777216
        n = (n ^ (n // 32)) % 16777216
        n = (n ^ (n * 2048)) % 16777216
        s.append(int(str(n)[-1])-pn)
        if len(s) > 4:
            s.pop(0)
            if not (s[0], s[1], s[2], s[3]) in v:
                v.add((s[0], s[1], s[2], s[3]))
                if not (s[0], s[1], s[2], s[3]) in d:
                    d[(s[0], s[1], s[2], s[3])] = 0
                d[(s[0], s[1], s[2], s[3])] += int(str(n)[-1])
print(max(d.values()))