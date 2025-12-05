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
inpB = [int(i) for i in inp[1].split("\n") if i]
inpA = [[int(a), int(b)] for a, b in inpA]

r = 0

for i in inpB:
    for a, b in inpA:
        if a <= i and i <= b:
            r += 1
            break

print(r)