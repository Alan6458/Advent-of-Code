inp = """
987654321111111
811111111111119
234234234234278
818181911112111
"""

inp = [i for i in inp.split("\n") if i]

r = 0

for i in inp:
    n = [k for k in i[-12:]]
    for j in range(len(i) - 13, -1, -1):
        if i[j] >= n[0]:
            nn = n.copy()
            for k in range(1, 12):
                if n[k-1] >= n[k]:
                    nn[k] = n[k-1]
                else:
                    break
            nn[0] = i[j]
            n = nn
    r += int("".join(n))

print(r)