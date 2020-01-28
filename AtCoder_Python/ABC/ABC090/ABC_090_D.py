# ABC090D
N, K = map(int, input().split())
ans = 0
cnt = 0

if K == 0:
    print(N ** 2)
    exit()

for b in range(K+1, N+1, 1):
    cnt += 1
    tmp = (N - (K + cnt - 1)) // b
    ans += cnt * (tmp + 1)
    if (tmp + 1) * b + K <= N:
        ans += N - ((tmp + 1) * b + K) + 1
    ##print(b, ans)

print(ans)