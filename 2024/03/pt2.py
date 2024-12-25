inp = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""

num1s = ""
num2s = ""
mulStage = 0
doStage = 0
dontStage = 0
digits = "0123456789"
r = 0
doAdd = True
doS = "do()"
dontS = "don't()"

for i in inp:
    if mulStage == 0:
        if i == "m":
            mulStage += 1
    elif mulStage == 1:
        if i == "u":
            mulStage += 1
        else:
            mulStage = 0
    elif mulStage == 2:
        if i == "l":
            mulStage += 1
        else:
            mulStage = 0
    elif mulStage == 3:
        if i == "(":
            mulStage += 1
        else:
            mulStage = 0
    elif mulStage == 4:
        if i in digits:
            num1s += i
        elif i == ",":
            mulStage += 1
        else:
            mulStage = 0
            num1s = ""
    elif mulStage == 5:
        if i in digits:
            num2s += i
        elif i == ")" and len(num1s) >= 1 and len(num1s) <= 3 and len(num2s) >= 1 and len(num2s) <= 3 and doAdd:
            r += int(num1s) * int(num2s)
            mulStage = 0
            num1s = ""
            num2s = ""
        else:
            mulStage = 0
            num1s = ""
            num2s = ""
    if i == doS[doStage]:
        doStage += 1
    else:
        doStage = 0
    if doStage == 4:
        doStage = 0
        doAdd = True
    if i == dontS[dontStage]:
        dontStage += 1
    else:
        dontStage = 0
    if dontStage == 7:
        dontStage = 0
        doAdd = False
print(r)