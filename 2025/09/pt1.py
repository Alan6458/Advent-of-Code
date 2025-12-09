inp = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

inp = [i.split(",") for i in inp.split("\n") if i]
inp = [[int(a), int(b)] for a, b in inp]

r = 0
for i in range(len(inp) - 1):
    for j in range(i + 1, len(inp)):
        a = (abs(inp[j][0] - inp[i][0]) + 1) * (abs(inp[j][1] - inp[i][1]) + 1)
        if a > r:
            r = a

print(r)