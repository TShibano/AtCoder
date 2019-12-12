# ABC015D
# Pytho3はTLE
# 方針：拡張ナップサック(幅制限+個数制限)
W = int(input())
N, K = map(int, input().split())
A = [0] * N
B = [0] * N
for _ in range(N):
    A[_], B[_] = map(int, input().split())

# dp[n][k][w] := SSがn-1枚ある時に，その中からk枚選んで幅wを超えない時の価値の最大値
dp = [[[0] * (W+1) for a in range(K+1)] for _ in range(N+1)]
dp[0][0][0] = 0

for n in range(N):
    for k in range(K+1):
        for w in range(W+1):
            if k == K:      # 枚数的に追加できない．
                dp[n+1][k][w] = max(dp[n][k][w], dp[n+1][k][w])
                continue
            if w + A[n] <= W:   # 幅が足りる時
                # 選ぶ
                dp[n+1][k+1][w+A[n]] = max(dp[n+1][k+1][w+A[n]], dp[n][k][w] + B[n])
            # 選ばない時
            dp[n+1][k][w] = max(dp[n+1][k][w], dp[n][k][w])
##print(dp)
print(dp[N][K][W])