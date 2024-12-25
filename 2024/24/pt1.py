inp = """
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
"""

inp = inp.split("\n\n")
inp = [i for i in inp if i]
inpA = inp[0].split("\n")
inpB = inp[1].split("\n")
inpA = [i for i in inpA if i]
inpB = [i for i in inpB if i]

vals = {}

for i in inpA:
    vals[i[:3]] = int(i[-1])

andL, orL, xorL = [], [], []
zL = []

for i in inpB:
    s = i.split(" ")
    if s[0] not in vals:
        vals[s[0]] = -1
    if s[2] not in vals:
        vals[s[2]] = -1
    if s[4] not in vals:
        vals[s[4]] = -1
    if s[4][0] == "z":
        zL.append(s[4])
    if s[1] == "AND":
        andL.append((s[0], s[2], s[4]))
    elif s[1] == "OR":
        orL.append((s[0], s[2], s[4]))
    elif s[1] == "XOR":
        xorL.append((s[0], s[2], s[4]))


zL = sorted(zL)
while any(vals[i] == -1 for i in zL):
    for a, b, c in andL:
        if vals[a] != -1 and vals[b] != -1 and vals[c] == -1:
            vals[c] = vals[a] & vals[b]
    for a, b, c in orL:
        if vals[a] != -1 and vals[b] != -1 and vals[c] == -1:
            vals[c] = vals[a] | vals[b]
    for a, b, c in xorL:
        if vals[a] != -1 and vals[b] != -1 and vals[c] == -1:
            vals[c] = vals[a] ^ vals[b]

print(int("".join(str(vals[i]) for i in zL)[::-1], 2))