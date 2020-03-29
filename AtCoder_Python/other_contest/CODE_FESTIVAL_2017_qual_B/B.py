# B
N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))
D.sort()
T.sort()
cnt = 0
ans = "YES"
for i in range(M):
    now = T[i]
    for j in range(cnt, N):
        if now > D[j]:
            pass
        elif now == D[j]:
            cnt = j+1
            break
        else:
            ans = "NO"
            break
print(ans)