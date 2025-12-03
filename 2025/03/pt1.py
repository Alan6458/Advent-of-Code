inp = """
987654321111111
811111111111119
234234234234278
818181911112111
"""

inp = [i for i in inp.split("\n") if i]

r = 0

for i in inp:
    n1, n2 = 0, int(i[-1])
    for j in range(len(i) - 2, -1, -1):
        if int(i[j]) >= n1:
            n2 = max(n2, n1)
            n1 = int(i[j])
    r += 10*n1 + n2

print(r)