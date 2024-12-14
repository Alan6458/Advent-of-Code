inp = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""

xLen, yLen = 101, 103
xLen, yLen = 11, 7
secs = 100

inp = inp.split("\n")
inp = [i for i in inp if i]
inp = [i.replace("p=", "").split(" v=") for i in inp]
inp = [[list(map(int, a.split(","))), list(map(int, b.split(",")))] for a, b in inp]

l = []
for [a, b], [c, d] in inp:
    l.append([(a + c*secs) % xLen, (b + d*secs) % yLen])

r1, r2, r3, r4 = 0, 0, 0, 0
for a, b in l:
    if a < xLen // 2 and b < yLen // 2:
        r1 += 1
    elif a > xLen // 2 and b < yLen // 2:
        r2 += 1
    elif a < xLen // 2 and b > yLen // 2:
        r3 += 1
    elif a > xLen // 2 and b > yLen // 2:
        r4 += 1
print(r1*r2*r3*r4)