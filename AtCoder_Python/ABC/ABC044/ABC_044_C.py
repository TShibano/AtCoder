# ABC044C
N, A = map(int, input().split())
X = list(map(int, input().split()))

# 2 ** 50 -> 全探索は厳しい -> DP
# dp[i][k][wa] = i枚まで見て、k枚選んだ時の合計値がwaとなるときの選び方の合計
# max wa = max(X) * N
max_wa = max(X) * N
dp = [[[0] * (max(X) * (N+1)) for _ in range(N+1)] for __ in range(N+1)]
dp[0][0][0] = 1
for i in range(N):
    for k in range(i+1):
        for wa in range(max_wa):
            # 選ぶとき
            dp[i+1][k+1][wa+X[i]] += dp[i][k][wa]
            # 選ばないとき
            dp[i+1][k][wa] += dp[i][k][wa]

ans = 0
for k in range(1, N+1):
    if k * A > max_wa:      # k*A が max_wa を超えた時点で打ち切り(dpのデータ確保が追いついていない場合を考慮)
        break
    ans += dp[-1][k][k*A]

print(ans)
