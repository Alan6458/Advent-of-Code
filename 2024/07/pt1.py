inp = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

inp = inp.split("\n")
inp = [i for i in inp if i != ""]
inp = [i.split(": ") for i in inp]
inp = [[int(a), list(map(int, b.split(" ")))] for a, b in inp]

r = 0

for a, b in inp:
    for i in range(2**(len(b)-1)):
        bC = b.copy()
        s = bC.pop(0)
        l = bin(i)[2:].zfill(len(b)-1)
        for j in l:
            if j == "0":
                s += bC.pop(0)
            else:
                s *= bC.pop(0)
        if s == a:
            r += a
            break
print(r)