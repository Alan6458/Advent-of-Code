inp = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

# I forgot to do Advent of Code when it started lol

inp = inp.split("\n\n")
inp1 = inp[0]
inp2 = inp[1]
inp1 = inp1.split("\n")
inp2 = inp2.split("\n")
inp1 = [i for i in inp1 if i != ""]
inp2 = [i for i in inp2 if i != ""]

inp1 = [[int(i[:2]), int(i[3:])] for i in inp1]
inp2 = [i.split(",") for i in inp2]
inp2 = [list(map(int, i)) for i in inp2]

bef = {i:set() for i in range(10, 100)}
aft = {i:set() for i in range(10, 100)}

for a, b in inp1:
    bef[a].add(b)
    aft[b].add(a)

r = 0

for i in inp2:
    correct = True
    for j, v in enumerate(i):
        if any(k in bef[v] for k in i[:j]) or any(k in aft[v] for k in i[j+1:]):
            correct = False
            break
    if correct:
        r += i[len(i) // 2]
print(r)