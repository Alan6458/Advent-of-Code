inp = """
"""

# This one takes a little manual work.

# Input will look like a circle with a slot inside. (a1, b1) is the upper-inner corner of the slot. (a2, b2) is the lower-inner corner of the slot.
a1, b1 = 0,0
a2, b2 = 0,0
# These are the upper and lower bounds of the rectangle.
# "upper" can be found by starting at (a1, b1) and going up to the next line. "upper" is the y-axis of that line.
# "lower" can be found by starting at (a2, b2) and going down to the next line. "lower" is the y-axis of that line.
upper = 0
lower = 0
# "minArea" is the lowest area to be considered for a possible answer. Tweak this value if you don't get enough answers.
minArea = 1000000000

# A plot will show up with a circle-like shape and rectangles with dotted perimeters inside.
# A list will be printed with area, x-coordinate of the second point, and y-coordinate of the second point.
# Check each rectangle (identified by the printed coordinate), going down the printed list to make sure that it is within the circle. The zoom feature will help.
# If it is not fully in the circle, go down to the next one. If it is fully in the circle, then you have your solution.

from matplotlib import pyplot as plt

inp = [i.split(",") for i in inp.split("\n") if i]
inp = [[int(a), int(b)] for a, b in inp]
inpA, inpB = [a for a, b in inp], [b for a, b in inp]

l = []

for a, b in inp:
    if b < b1 or b > upper:
        continue
    area = (abs(a1 - a) + 1) * (abs(b1 - b) + 1)
    if area > minArea:
        c, d = a, b
        e, f = a1, b1
        l.append((area, c, d, e, f))

for a, b in inp:
    if b > b2 or b < lower:
        continue
    area = (abs(a2 - a) + 1) * (abs(b2 - b) + 1)
    if area > minArea:
        c, d = a, b
        e, f = a2, b2
        l.append((area, c, d, e, f))

l = sorted(l, reverse=True)

plt.plot(inpA, inpB)
print("Area, X coord, Y coord")
for area, c, d, e, f in l:
    print(area, e, f)
    plt.plot([c, c, e, e, c], [f, d, d, f, f], ":")
plt.show()