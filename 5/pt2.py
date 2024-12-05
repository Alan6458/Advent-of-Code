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

# This might be the first problem I consider "harder" and not just "tedious"
# Part 2 took me a whole 30 minutes

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
inp1a, inp1b = [i[0] for i in inp1], [i[1] for i in inp1]

bef = {i:set() for i in range(10, 100)}
aft = {i:set() for i in range(10, 100)}

for a, b in inp1:
    bef[a].add(b)
    aft[b].add(a)

# My attempts to have a pre-sorted ordering
# (Did not work on my actual given input but did on the test input)

# d = [10]
# for i in range(11, 100):
#     for j in range(len(d)+1):
#         if all(k not in bef[i] for k in d[:j]) and all(k not in aft[i] for k in d[j:]):
#             d.insert(j, i)
#             print("s", i)
#             break
#     else:
#         print(i)
# print([i for i in d if len(bef[i]) or len(aft[i])])
# for i in range(10, 100):
#     if inp1a.count(i):
#         print(inp1a.count(i))
# d = sorted(list(range(10, 100)), key=lambda i:inp1b.count(i))
# print([i for i in d if len(bef[i]) or len(aft[i])])
# d = {v:i for i, v in enumerate(d)}

r = 0

for i in inp2:
    correct = True
    for j, v in enumerate(i):
        if any(k in bef[v] for k in i[:j]) or any(k in aft[v] for k in i[j+1:]):
            correct = False
            break
    if not correct:
        d = []
        for j in i:
            if len(d) == 0:
                d.append(j)
                continue
            for k in range(len(d)+1):
                if all(l not in bef[j] for l in d[:k]) and all(l not in aft[j] for l in d[k:]):
                    d.insert(k, j)
                    break
        d = {v:i for i, v in enumerate(d)}
        i = sorted(i, key=lambda a:d[a])
        r += i[len(i) // 2]
print(r)