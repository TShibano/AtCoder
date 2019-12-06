# Typical DP contest B
# https://www.creativ.xyz/tdpc-b-684/
# を参考にした
# DPはテストケースで遷移を考える!

A, B = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

# DPテーブル
# dp[i][j] := Aにi個，Bにj個残っている時の先手の最適スコア
dp = [[0] * (B+1) for _ in range(A+1)]
dp[A][B] = 0

for i in range(A, -1, -1):
    for j in range(B, -1, -1):
        if i == A and j == B:   # 初期状態
            continue

        if (i+j) % 2 == 0:      # 先手のターン
            if i == A:          # Aの山が空
                dp[i][j] = dp[i][j+1] + b_list[j]
            elif j == B:        # Bの山が空
                dp[i][j] = dp[i+1][j] + a_list[i]
            else:
                # 先手は最大になるように取る
                dp[i][j] = max(dp[i+1][j] + a_list[i], dp[i][j+1] + b_list[j])

        else:                   # 後手のターン
            if i == A:          # Aの山が空
                dp[i][j] = dp[i][j+1]
            elif j == B:        # Bの山が空
                dp[i][j] = dp[i+1][j]
            else:
                # 後手は先手のスコアが最小になるように取る
                dp[i][j] = min(dp[i+1][j], dp[i][j+1])

print(dp[0][0])