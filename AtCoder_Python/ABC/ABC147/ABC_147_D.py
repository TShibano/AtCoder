# ABC147D
mod = 10**9 + 7
N = int(input())
A = list(map(int, input().split()))
ans = 0

for i in range(61):
    tmp_1 = 0
    tmp_0 = 0
    for k in range(N):
        if (A[k] >> i) & 1:
            tmp_1 += 1
        else:
            tmp_0 += 1
    ##print(i, tmp_1, tmp_0)
    ans += (tmp_1 * tmp_0) * (2 ** i)
print(ans%mod)