inp = "125 17"

inp = inp.split(" ")

inpNew = []

for i in range(25):
    for j in inp:
        if j == "0":
            inpNew.append("1")
        elif len(j) % 2 == 0:
            inpNew.append(j[:len(j)//2])
            inpNew.append(str(int(j[len(j)//2:])))
        else:
            inpNew.append(str(int(j)*2024))
    inp = inpNew.copy()
    inpNew = []

print(len(inp))