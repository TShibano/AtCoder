# TypicalDPContest-A
# 方針：部分和問題に帰着し，0 ~ max値までを作れるかを調べる．
# そしてその数を調べる
N = int(input())
p = list(map(int, input().split()))

max_value = N * max(p)

# DPテーブル
dp = [[False] * (max_value + 10) for _ in range(N+10)]

dp[0][0] = True
for i in range(N):
    for j in range(max_value+1):
        if j >= p[i]:
            dp[i+1][j] = dp[i][j - p[i]] or dp[i][j]
        else:
            dp[i+1][j] = dp[i][j]

ans = 0
for j in range(0, max_value+1):
    if dp[N][j]:
        ans += 1

print(ans)