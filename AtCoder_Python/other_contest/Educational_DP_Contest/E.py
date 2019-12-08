# # Educational DP Contest E
# 方針：dp[i][v] := i-1番目までの物の中から，価値v以上を達成するように選んだ時の重さの最小値

# 入力
N, W = map(int, input().split())
weight = [0] * N
value = [0] * N
for i in range(N):
    w, v = map(int, input().split())
    weight[i] = w
    value[i] = v

# DPテーブル
max_v = sum(value)
dp = [[float("inf")] * (max_v + 1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for v in range(max_v+1):
        if v >= value[i]:       # i番目の物を選ぶ時
            dp[i+1][v] = min(dp[i][v - value[i]] + weight[i], dp[i][v])
        else:
            dp[i+1][v] = dp[i][v]

for v in range(max_v, -1, -1):
    if dp[N][v] <= W:
        ans = v
        break
print(ans)