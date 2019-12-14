# Typical DP Contest E
# Python3だとTLE
mod = 1000000007
D = int(input())
N = input()

keta = len(N)

# dp[i][j][smaller] := i桁目まで追加して，mod Dの和をjとする方法は何通りあるか，
# smaller : Nより小さいと言うことが確定している場合は1．未確定なら0
# 今の見ている数字N[i]とk(0-9)の組み合わせについて場合で遷移を分ける
dp = [[[0] * 2 for _ in range(D)] for __ in range(keta+1)]
first_keta = int(N[0])
dp[0][0][0] = 1

for i in range(keta):
    now_digit = int(N[i])
    for j in range(D):
        for k in range(10):
            tmp = (j+k)%D
            if k < now_digit:
                dp[i+1][tmp][1] += (dp[i][j][0] + dp[i][j][1]) % mod
                dp[i+1][tmp][1] %= mod
            elif now_digit == k:
                dp[i+1][tmp][1] += dp[i][j][1]
                dp[i+1][tmp][0] += dp[i][j][0]
                dp[i+1][tmp][1] %= mod
                dp[i+1][tmp][0] %= mod
            else:
                dp[i+1][tmp][1] += dp[i][j][1]
                dp[i+1][tmp][1] %= mod

##print(dp)
print((dp[-1][0][0] + dp[-1][0][1] - 1 + mod)%mod)