inp = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

inp = inp.split("\n\n")
inp = [i.split("\n") for i in inp if i]
inp = [[j for j in i if j] for i in inp]
inp = [[list(map(int, a.replace("Button A: X+", "").split(", Y+"))), list(map(int, b.replace("Button B: X+", "").split(", Y+"))), list(map(int, c.replace("Prize: X=", "").split(", Y=")))] for a, b, c in inp]

r = 0

ma, mb = 0, 0
man, mad, mbn, mbd = 0, 0, 0, 0

for [ax, ay], [bx, by], [px, py] in inp:
    px += 10000000000000
    py += 10000000000000
    mbn = ax*py-ay*px
    mbd = ax*by-ay*bx
    man = bx*py-by*px
    mad = bx*ay-by*ax
    # I spent a half hour focusing on a nonexistent edge case where mad == 0 or mbd == 0
    ma, mb = man/mad, mbn/mbd
    if ma == round(ma) and mb == round(mb) and ma >= 0 and mb >= 0:
        r += 3 * ma + mb
print(round(r))