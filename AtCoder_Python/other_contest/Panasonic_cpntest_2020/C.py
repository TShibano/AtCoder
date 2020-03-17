# C
a, b, c = map(int, input().split())
# a + b + 2(ab)**0.5 < c
# c - a - b > 2(ab)**-.5
tmp = c - a - b
if tmp < 0 :
    print("No")
    exit()
if tmp ** 2 > 4 * a * b:
    print("Yes")
else:
    print("No")