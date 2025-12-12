inp = """"""

inp = [i for i in inp.split("\n\n") if i]
l = inp.pop(-1)
inp = [i.count("#") for i in inp]
l = [i for i in l.split("\n") if i]

l1 = [int(i[0:2]) * int(i[3:5]) for i in l]
l2 = [list(map(int, i.split(" ")[1:])) for i in l]
l2 = [sum([i[j] * inp[j] for j in range(len(i))]) for i in l2]

print(sum([1 for i in range(len(l1)) if l1[i] > l2[i]]))