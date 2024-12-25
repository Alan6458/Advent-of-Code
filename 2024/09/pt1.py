inp = "2333133121414131402"

inp1 = [i for i in inp[::2]]
inp1 = [i for i, v in enumerate(inp1) for _ in range(int(v))]

r = 0
ind = 0
for i, v in enumerate(inp):
    for j in range(int(v)):
        if len(inp1) == 0:
            break
        if i % 2:
            r += ind * inp1.pop(-1)
        else:
            r += ind * inp1.pop(0)
        ind += 1
    if len(inp1) == 0:
        break
print(r)