# JOI2007yosenA
N = 1000 - int(input())

ans = 0
while N >= 500:
    ans += 1
    N -= 500

while N >= 100:
    ans += 1
    N -= 100

while N >= 50:
    ans += 1
    N -= 50

while N >= 10:
    ans += 1
    N -= 10

while N >= 5:
    ans += 1
    N -= 5

print(ans + N)

# 解説の解き方-していることは同じ
N = 1000 - int(input())
ans = 0

ans += N // 500
N %= 500

ans += N // 100
N %= 100

ans += N // 50
N %= 50

ans += N // 10
N %= 10

ans += N // 5
N %= 5

print(ans + N)