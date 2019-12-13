# JOI2012-D
# dp[d][n] := d日においてn番目の服を着たときの，派手さの絶対値の最大値
# dp[d][n] = max(dp[d-1][k] + abs(C[k] - C[n]))
D, N = map(int, input().split())
T = [int(input()) for _ in range(D)]
A = [0] * N
B = [0] * N
C = [0] * N
for _ in range(N):
    a, b, c = map(int, input().split())
    A[_] = a
    B[_] = b
    C[_] = c

# dpテーブル
dp = [[0] * N for _ in range(D)]
# 初期化
for n in range(N):
    if A[n] <= T[0] <= B[n]:
        continue
    else:
        dp[0][n] = -float("inf")

for d in range(1, D):
    for n in range(N):
        if A[n] <= T[d] <= B[n]:
            tmp_list = [0] * N
            for k in range(N):
                tmp_list[k] = dp[d-1][k] + abs(C[k] - C[n])
            dp[d][n] = max(tmp_list)
        else:
            dp[d][n] = -float("inf")

print(max(dp[D-1]))