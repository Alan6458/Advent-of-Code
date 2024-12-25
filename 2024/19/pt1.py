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
    l = [True] + [False for _ in range(len(i))]
    for j, v in enumerate(i):
        if l[j] == False:
            continue
        for k in range(1, 8):
            if j + k > len(i):
                break
            if i[j:j+k] in available:
                l[j+k] = True
    if l[-1] == True:
        r += 1
print(r)