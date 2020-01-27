# ABC153E
H, N = map(int, input().split())
A = [0] * N
B = [0] * N 
for i in range(N):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b

# dp[i][h] := i-1 番目の魔法の中から，減らす体力が h を達成するように選んだ時の魔法の最小値
# DP テーブル
dp = [[float("inf")] * (H + 1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for h in range(H + 1):
        dp[i+1][h] = min(dp[i][h], dp[i+1][h])
        if h - A[i] >= 0:       # 選ぶ時
            dp[i+1][h] = min(dp[i+1][h - A[i]] + B[i], dp[i][h])
        else: 
            # 選べない時は i-1 枚目の魔法で埋める
            dp[i+1][h] = min(dp[i][0] + B[i], dp[i+1][h])
            
for i in range(N+1):
    print(dp[i])


print(dp[N][H])