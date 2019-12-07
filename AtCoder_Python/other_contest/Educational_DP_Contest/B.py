# # Educational DP Contest B
# 方針：dp[i] := 足場iにくるまでの最小コスト
# 足場iに来るにはi-1, i-2, ..., i-kを考える(k = 1, 2, ..., K)
N, K = map(int, input().split())
H = list(map(int, input().split()))

dp = [float("inf")] * N
dp[0] = 0

for i in range(1, N):
    cost_list = [float("inf")] * K      # iに来る時ののコストのリストを作成する
    for k in range(1, K+1):
        if i - k < 0:
            break
        cost_list[k-1] = dp[i-k] + abs(H[i] - H[i-k])
    dp[i] = min(cost_list)
print(dp[N-1])