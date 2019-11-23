# DDCC2020A
X, Y = map(int, input().split())
first = 300000
second = 200000
third = 100000
ans = 0
if X == 1 and Y == 1:
    print(300000 + 300000 + 400000)
    exit()
if X == 1:
    ans += first
elif X == 2:
    ans += second
elif X == 3:
    ans += third
else:
    ans += 0

if Y == 1:
    ans += first
elif Y == 2:
    ans += second
elif Y == 3:
    ans += third
else:
    ans += 0

print(ans)
