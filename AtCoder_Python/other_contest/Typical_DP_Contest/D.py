# Typical DP Contest D
N, D = map(int, input().split())

# Dは2 or 3 or 5しか持ってはいけない．7や11などはダメ
d2 = 0
d3 = 0
d5 = 0
while D % 2 == 0:
    D //= 2
    d2 += 1
while D % 3 == 0:
    D //= 3
    d3 += 1
while D % 5 == 0:
    D //= 5
    d5 += 1
if D != 1:
    print("{:.10f}".format(0))
    exit()
# dpテーブル
# dp[i][c2][c3][c5] := (i+1)回サイコロを振った時の2の倍数がc2回，3の倍数がc3，5の倍数がc5回出る確率
dp = [[[[0] * (d5+1) for a in range(d3+1)] for b in range(d2+1)] for c in range(N+1)]

# 初期条件
dp[0][0][0][0] = 1

for i in range(N):
    for c2 in range(d2+1):
        for c3 in range(d3+1):
            for c5 in range(d5+1):
                # 配るDP．上から順に1 ~ 6の目がでた時に次の確率．
                # もしd2, d3, d5より大きくなったら全てd2, d3, d5に格納する
                dp[i+1][c2][c3][c5] += dp[i][c2][c3][c5] / 6
                dp[i+1][min(c2+1, d2)][c3][c5] += dp[i][c2][c3][c5] / 6
                dp[i+1][c2][min(c3+1, d3)][c5] += dp[i][c2][c3][c5] / 6
                dp[i+1][min(c2+2, d2)][c3][c5] += dp[i][c2][c3][c5] / 6
                dp[i+1][c2][c3][min(c5+1, d5)] += dp[i][c2][c3][c5] / 6
                dp[i+1][min(c2+1, d2)][min(c3+1, d3)][c5] += dp[i][c2][c3][c5] / 6

print("{:.10f}".format(dp[N][d2][d3][d5]))