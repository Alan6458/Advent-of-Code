inp = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

inp = inp.split("\n")
inp = [i for i in inp if i != ""]
inp = [i.split(" ") for i in inp]
inp = [list(map(int, i)) for i in inp]
r = 0
for i in inp:
    if (all(i[j] < i[j+1] for j in range(len(i)-1)) or all(i[j] > i[j+1] for j in range(len(i)-1))) and all(abs(i[j] - i[j+1]) <= 3 for j in range(len(i)-1)):
        r += 1
print(r)