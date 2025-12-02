inp = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

inp = [i for i in inp.split(",") if i]
inp = [i.split("-") for i in inp]
inp = [[int(a), int(b)] for a, b in inp]

done = set()

r = 0
for a, b in inp:
    for i in range(a, b + 1):
        s = str(i)
        for j in range(1, len(s)//2 + 1):
            n = len(s) // j
            if len(s) % j == 0:
                # Don't ask me how the following line works, I don't know either (I should stop using single character variables)
                if all(s[j*k:j*(k+1)] == s[j*(k+1):j*(k+2)] for k in range(len(s)//j - 1)) and i not in done:
                    r += i
                    done.add(i)

print(r)