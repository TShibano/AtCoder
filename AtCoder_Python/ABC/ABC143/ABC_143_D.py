# ABC143D
import bisect
N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
cnt = 0
for i in range(N - 2):
    for k in range(i + 1, N - 1):
        tmp = bisect.bisect_left(L, L[i] + L[k])
        ans += max(tmp - 1 - k, 0)
        # ans += bisect.bisect_left(L, L[i] + L[k]) - k - 1
        # で良い->0いかになることはない．最小の場合は隣にくるから

print(ans)