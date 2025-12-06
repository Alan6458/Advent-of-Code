inp = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

inp = [i.split(" ") for i in inp.split("\n") if i]
inp = [[j for j in i if j] for i in inp]

r = 0

for i in range(len(inp[0])):
    l = []
    for j in range(len(inp) - 1):
        l.append(int(inp[j][i]))
    if inp[-1][i] == "*":
        n = 1
        for k in l:
            n *= k
        r += n
    else:
        for k in l:
            r += k

print(r)