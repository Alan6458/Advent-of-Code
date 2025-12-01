inp = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

inp = [i for i in inp.split("\n") if i]
inp = [int(i[1:]) * (1 if i[0] == "R" else -1) for i in inp]

n = 50
r = 0

for i in inp:
    for j in range(abs(i)):
        n += i / abs(i)
        if n == 0:
            r += 1
        elif n == 100:
            n = 0
            r += 1
        if n < 0:
            n = 99

print(r)