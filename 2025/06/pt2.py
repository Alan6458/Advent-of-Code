inp = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

inp = [i for i in inp.split("\n") if i]

ops = [i.split() for i in inp[-1]]
ops = [i[0] for i in ops if i]

inpN = [[] for i in range(len(inp) - 1)]
last = 0
for i in range(1, len(inp[0])):
    if inp[-1][i] != " ":
        for j in range(len(inp) - 1):
            inpN[j].append(inp[j][last:i-1])
        last = i
for j in range(len(inp) - 1):
    inpN[j].append(inp[j][last:])
inp = inpN

r = 0

for i in range(len(inp[0])):
    l = []
    m = 0
    for j in range(len(inp)):
        l.append(inp[j][i])
        m = max(m, len(inp[j][i]))
    nl = [""] * m
    for k in l:
        for ind, v in enumerate(k):
            nl[ind] += v
    l = [int(z) for z in nl]
    if ops[i] == "*":
        n = 1
        for k in l:
            n *= k
        r += n
    else:
        for k in l:
            r += k

print(r)