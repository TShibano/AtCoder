# ABC029D
# ABC029D
N = input()
keta = len(N)
# dp[i]j[cnt][smaller] = i桁目までに1が出た数字の数
# cnt : 1が出た個数をカウント
# smaller = 0, 1で1が小さいことが確定している，0は未確定
dp = [[[0] * 2 for _ in range(10)] for __ in range(keta+1)]
##dp = [[0] * 2 for _ in range(keta+1)]
dp[0][0][0] = 1

for i in range(keta):
    now_digit = int(N[i])
    for cnt in range(9):
        for k in range(10):
            if k == 1:
                if k < now_digit:
                    dp[i+1][cnt+1][1] += dp[i][cnt][1] + dp[i][cnt][0]
                elif k == now_digit:
                    dp[i+1][cnt+1][1] += dp[i][cnt][1]
                    dp[i+1][cnt+1][0] += dp[i][cnt][0]
                else:
                    dp[i+1][cnt+1][1] += dp[i][cnt][1]
            else:
                if k < now_digit:
                    dp[i+1][cnt][1] += dp[i][cnt][0] + dp[i][cnt][1]

                elif k == now_digit:
                    dp[i+1][cnt][1] += dp[i][cnt][1]
                    dp[i+1][cnt][0] += dp[i][cnt][0]
                else:
                    dp[i+1][cnt][1] += dp[i][cnt][1]
ans = 0
for cnt in range(10):
    ans += cnt * (dp[-1][cnt][1] + dp[-1][cnt][0])
print(ans)