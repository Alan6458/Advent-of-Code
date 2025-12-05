inp = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

inp = inp.split("\n\n")
inpA = [i.split("-") for i in inp[0].split("\n") if i]
inpA = [[int(a), int(b)] for a, b in inpA]

inpA = sorted(inpA)
r = 0

tor = []
for i in range(1, len(inpA)):
    if inpA[i][1] <= inpA[i-1][1]:
        tor.append(i)
inpA = [v for i, v in enumerate(inpA) if i not in tor]

for i in range(len(inpA) - 1):
    inpA[i][1] = min(inpA[i][1], inpA[i+1][0] - 1)
    r += inpA[i][1] - inpA[i][0] + 1
r += inpA[-1][1] - inpA[-1][0] + 1

print(r)