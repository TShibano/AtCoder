# # Educational DP Contest D
# 方針：dp[i][w] := i番目の物の中から，重さwを超えない時の価値の最大値
N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (W+10) for _ in range(N+1)]

for i in range(N):
    for w in range(W+1):
        if w >= wv[i][0]:       # 重さwv[i][0]を入れられるか
            dp[i+1][w] = max(dp[i][w - wv[i][0]] + wv[i][1], dp[i][w])
        else:
            dp[i+1][w] = dp[i][w]
print(dp[N][W])