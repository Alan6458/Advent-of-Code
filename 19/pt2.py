inp = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""

inp = inp.split("\n\n")
inp = [i for i in inp if i]
available = set(inp[0].replace("\n", "").split(", "))
inp = inp[1].split("\n")
inp = [i for i in inp if i]

r = 0
for i in inp:
    l = [1] + [0 for _ in range(len(i))]
    for j, v in enumerate(i):
        for k in range(1, 9):
            if j + k > len(i):
                break
            if i[j:j+k] in available:
                l[j+k] += l[j]
    r += l[-1]
print(r)