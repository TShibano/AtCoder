# ABC146C
def get_keta(N):
    ans = 1
    while True:
        if N // 10 != 0:
            ans += 1
            N //= 10
        if N // 10 == 0:
            break
    return ans

A, B, X = map(int, input().split())
if A * (10 ** 9) + B * 10 <= X:
    print(10 ** 9)
    exit()
for i in range(9, 0, -1):
    tmp = 10 ** (i-1)
    if A * tmp + B * i <= X:
        keta = i
        break
    if i == 1:
        print(0)
        exit()

ans = (X - B * keta) // A
if get_keta(ans) != keta:
    ans -= 1
    print(ans)
    exit()

if ans >= 10 ** 9:
    ans = 10 ** 9
if ans <= 0:
    ans = 0
print(ans)
