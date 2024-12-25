inp = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""

inp = inp.split("\n")
inp = [i for i in inp if i]
inpA = int(inp[0].replace("Register A: ", ""))
inpB = int(inp[1].replace("Register B: ", ""))
inpC = int(inp[2].replace("Register C: ", ""))
inp = list(map(int, inp[3].replace("Program: ", "").split(",")))

rN = 0
inpA = 0
r = [-1]
for pwr in range(len(inp)):
    rNN = 1
    inpA = inpA * 8
    while any(r[j] != inp[len(inp)-len(r)+j] for j in range(len(r))) or rNN:
        rNN = 0
        ops = [0, 1, 2, 3, inpA, inpB, inpC]

        i = 0
        r = []
        while i < len(inp):
            if inp[i] == 0:
                ops[4] = ops[4] // (2 ** ops[inp[i+1]])
                i += 2
            elif inp[i] == 1:
                ops[5] = ops[5] ^ inp[i+1]
                i += 2
            elif inp[i] == 2:
                ops[5] = ops[inp[i+1]] % 8
                i += 2
            elif inp[i] == 3:
                if ops[4]:
                    i = inp[i+1]
                else:
                    i += 2
            elif inp[i] == 4:
                ops[5] = ops[5] ^ ops[6]
                i += 2
            elif inp[i] == 5:
                r.append(ops[inp[i+1]]%8)
                i += 2
            elif inp[i] == 6:
                ops[5] = ops[4] // (2 ** ops[inp[i+1]])
                i += 2
            elif inp[i] == 7:
                ops[6] = ops[4] // (2 ** ops[inp[i+1]])
                i += 2
        while len(r) < pwr + 1:
            r.insert(0, 0)
        if any(r[j] != inp[len(inp)-len(r)+j] for j in range(len(r))):
            inpA += 1
print(inpA)