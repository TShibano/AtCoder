# B
mod = 10 ** 9 + 7
N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt_list = [[0, 0] for _ in range(N)]
for i in range(N):
    right = 0
    left = 0
    for j in range(N):
        if i < j:       # right
            if A[i] > A[j]:
                right += 1
        else:           # left
            if A[i] > A[j]:
                left += 1
    cnt_list[i][0] = left
    cnt_list[i][1] = right
ans = 0
for i in range(N):
    left = cnt_list[i][0]
    right = cnt_list[i][1]
    ans += left * (K - 1) * K // 2
    ans += right *  K * (K + 1) // 2
    ans %= mod
print(ans)