inp = "2333133121414131402"

# This took WAYYYY too long...

lInp = len(inp)

inp = [[-1 if i % 2 else i // 2, int(v)] for i, v in enumerate(inp) if int(v)]

for i in range(-(-lInp//2)-1, -1, -1):
    while inp[-1][0] == -1:
        inp.pop(-1)
    ind = len(inp)-1
    while inp[ind][0] != i:
        ind -= 1
    for j in range(ind):
        if inp[j][0] == -1 and inp[j][1] >= inp[ind][1]:
            inp[j][1] -= inp[ind][1]
            inp.insert(j, inp[ind].copy())
            inp[ind+1][0] = -1
            if inp[j+1][1] == 0:
                inp.pop(j+1)
            if len(inp) > ind+2:
                if inp[ind+1][0] == -1 and inp[ind+2][0] == -1:
                    inp[ind+1][1] += inp.pop(ind+2)[1]
            if len(inp) > ind+1:
                if inp[ind+1][0] == -1 and inp[ind][0] == -1:
                    inp[ind+1][1] += inp.pop(ind)[1]
            if inp[ind][0] == -1 and inp[ind-1][0] == -1:
                inp[ind][1] += inp.pop(ind-1)[1]
            break
r = 0
ind = 0
for a, b in inp:
    if a == -1:
        ind += b
        continue
    for j in range(b):
        r += ind * a
        ind += 1
print(r)