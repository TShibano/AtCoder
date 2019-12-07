# Educational DP Contest A
# 方針：dp[i] := 足場iに来るまでの最小コスト
# 足場iに来るには，i-2から飛んでくるか，i-1から飛んでくるか
N = int(input())
H = list(map(int, input().split()))

dp = [float("inf")] * N         # 最小化問題なのでINFで初期化
dp[0] = 0
dp[1] = abs(H[0] - H[1])
for i in range(2, N):
    dp[i] = min(dp[i-2] + abs(H[i] - H[i-2]), 
                dp[i-1] + abs(H[i] - H[i-1])
                )
print(dp[N-1])