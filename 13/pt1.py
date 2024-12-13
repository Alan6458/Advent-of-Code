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

for [ax, ay], [bx, by], [px, py] in inp:
    s = -1
    for i in range(px // bx + 1):
        if (px - i * bx) % ax == 0 and (py - i * by) % ay == 0 and (px - i * bx) / ax == (py - i * by) / ay:
            if i + 3 * ((px - i * bx) // ax) < s or s == -1:
                s = i + 3 * ((px - i * bx) // ax)
    if s > 0:
        r += s
print(r)