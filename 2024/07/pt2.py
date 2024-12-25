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

def trinary(n):
    if n == 0:
        return "0"
    rtn = []
    while n:
        rtn.append(str(n % 3))
        n = n // 3
    return "".join(rtn[::-1])

inp = inp.split("\n")
inp = [i for i in inp if i != ""]
inp = [i.split(": ") for i in inp]
inp = [[int(a), list(map(int, b.split(" ")))] for a, b in inp]

r = 0

for a, b in inp:
    for i in range(3**(len(b)-1)):
        # I forgot that operations were interpreted in order lol

        # bC1 = b.copy()
        # bC = [str(bC1.pop(0))]
        # l1 = list(trinary(i).zfill(len(b)-1))
        # l = []
        # for j in range(len(l1)):
        #     if l1[j] == "2":
        #         bC[-1] += str(bC1[j])
        #     else:
        #         l.append(l1[j])
        #         bC.append(str(bC1[j]))
        # bC = list(map(int, bC))
        # s = bC.pop(0)
        
        bC = b.copy()
        s = bC.pop(0)
        l = trinary(i).zfill(len(b)-1)
        for j in l:
            if j == "0":
                s += bC.pop(0)
            elif j == "1":
                s = int(str(s)+str(bC.pop(0)))
            else:
                s *= bC.pop(0)
        if s == a:
            r += a
            break
print(r)