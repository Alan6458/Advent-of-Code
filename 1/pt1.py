s = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

s = s.split("\n")
s = [i for i in s if i != ""]
s = [i.split("   ") for i in s]
s1 = [int(i[0]) for i in s]
s2 = [int(i[1]) for i in s]
s1 = sorted(s1)
s2 = sorted(s2)
r = 0
for i in range(len(s)):
    r += abs(s1[i]-s2[i])
print(r)
