# A
X, Y = map(int, input().split())
k = 1
if X % Y == 0:
    print(-1)
    exit()
while 1:
    if (k * X) % Y == 0:
        k += 1
    else:
        ans = k * X
        break
print(ans)