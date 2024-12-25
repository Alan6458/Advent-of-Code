inp = """
1
10
100
2024
"""

inp = inp.split("\n")
inp = [i for i in inp if i]
inp = list(map(int, inp))

r = 0
for i in inp:
    n = i
    for j in range(2000):
        n = (n ^ (n * 64)) % 16777216
        n = (n ^ (n // 32)) % 16777216
        n = (n ^ (n * 2048)) % 16777216
    r += n
print(r)