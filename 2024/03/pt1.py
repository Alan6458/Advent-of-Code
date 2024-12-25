inp = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

num1s = ""
num2s = ""
mulStage = 0
digits = "0123456789"
r = 0

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
        elif i == ")" and len(num1s) >= 1 and len(num1s) <= 3 and len(num2s) >= 1 and len(num2s) <= 3:
            r += int(num1s) * int(num2s)
            mulStage = 0
            num1s = ""
            num2s = ""
        else:
            mulStage = 0
            num1s = ""
            num2s = ""
print(r)