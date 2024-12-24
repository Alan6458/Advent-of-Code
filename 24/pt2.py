inp = """
"""

# I had to comb through my input lol
# But I fixed it by adding a little to one line

inp = inp.split("\n\n")
inp = [i for i in inp if i]
inpA = inp[0].split("\n")
inpB = inp[1].split("\n")
inpA = [i for i in inpA if i]
inpB = [i for i in inpB if i]

xL, yL = [], []

for i in inpA:
    if i[0] == "x":
        xL.append(i[:3])
    elif i[0] == "y":
        yL.append(i[:3])

andL, orL, xorL = [], [], []
zL = []
cL, exL, caL, anL = [""] * len(xL), [""] * len(xL), [""] * len(xL), [""] * len(xL)
gtAnd, gtOr, gtXor = set(), set(), set()
cfXor, cfAnd, cfOr = set(), set(), set()

for i in inpB:
    s = i.split(" ")
    if s[0][0] == "y" and s[2][0] == "x":
        s[0], s[2] = s[2], s[0]
    if s[4][0] == "z":
        zL.append(s[4])
    if s[1] == "AND":
        andL.append((s[0], s[2], s[4]))
        gtAnd.add(s[0])
        gtAnd.add(s[2])
        cfAnd.add(s[4])
    elif s[1] == "OR":
        orL.append((s[0], s[2], s[4]))
        gtOr.add(s[0])
        gtOr.add(s[2])
        cfOr.add(s[4])
    elif s[1] == "XOR":
        xorL.append((s[0], s[2], s[4]))
        gtXor.add(s[0])
        gtXor.add(s[2])
        cfXor.add(s[4])
zL = sorted(zL)
xL = sorted(xL)
yL = sorted(yL)

r = set()

for a, b, c in xorL:
    if a[0] == "x" and b[0] == "y":
        exL[int(a[1:3])] = c

for a, b, c in andL:
    if a[0] == "x" and b[0] == "y":
        anL[int(a[1:3])] = c

for i in zL:
    if (i == zL[-1] and i not in cfOr) or (i != zL[-1] and i not in cfXor) or i in cfAnd:
        r.add(i)

for i in exL[1:]:
    if i not in gtXor or i not in gtAnd or i in gtOr:
        r.add(i)

for i in anL[1:]:
    if i not in gtOr or i in gtXor or i in gtAnd:
        r.add(i)

for i in gtOr:
    if i not in cfAnd or i in gtAnd or i in gtXor:
        r.add(i)

for i in gtAnd:
    if i not in xL and i not in yL and (i not in gtXor or (i not in cfOr and i not in cfXor)) and i != anL[0]:
        r.add(i)

for i in gtXor:
    if i != anL[0] and i not in xL and i not in yL and (i not in gtAnd or (i not in cfOr and i not in cfXor)):
        r.add(i)

for i in cfOr:
    if i != zL[-1] and (i not in gtXor or i not in gtAnd or i in gtOr):
        r.add(i)

for i in cfXor:
    if i not in zL and (i not in gtXor or i not in gtAnd or i in gtOr or i not in exL):
        r.add(i)

for i in cfAnd:
    if i != anL[0] and (i in gtAnd or i in gtXor or i not in gtOr):
        r.add(i)

print(",".join(sorted(list(r))))