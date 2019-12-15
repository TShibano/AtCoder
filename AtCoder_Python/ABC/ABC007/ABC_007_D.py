# ABC007D
# 方針：桁DP
# Nまで求める関数を作ってf(B) - f(A-1)

A, B = map(str, input().split())

def solve(N):
    keta = len(N)
    # dp[i][j][smaller] := i桁目まで追加して，4と9を含まない数字の個数
    # j : すでに4もしくは9が出ている場合は1，出ていないなら0
    # smaller : Nより小さいと言うことが確定している場合は1，未確定なら0
    dp = [[[0] * 2 for _ in range(2)] for __ in range(keta+1)]
    dp[0][0][0] = 1
    for i in range(keta):
        now_digit = int(N[i])
        for k in range(10):
            if k == 4 or k == 9:
                if k < now_digit:
                    dp[i+1][1][1] += dp[i][0][1] + dp[i][0][0] + dp[i][1][1] + dp[i][1][0]
                elif k == now_digit:
                    dp[i+1][1][1] += dp[i][0][1] + dp[i][1][1]
                    dp[i+1][1][0] += dp[i][1][0] + dp[i][0][0]
                else:
                    dp[i+1][1][1] += dp[i][0][1] + dp[i][1][1]
            else:
                if k < now_digit:
                    dp[i+1][0][1] += dp[i][0][1] + dp[i][0][0]
                    
                    dp[i+1][1][1] += dp[i][1][1] + dp[i][1][0]
                elif k == now_digit:
                    dp[i+1][0][1] += dp[i][0][1]
                    dp[i+1][0][0] += dp[i][0][0]
                    
                    dp[i+1][1][1] += dp[i][1][1]
                    dp[i+1][1][0] += dp[i][1][0]
                else:
                    dp[i+1][0][1] += dp[i][0][1]

                    dp[i+1][1][1] += dp[i][1][1]
    return dp[-1][1][0] + dp[-1][1][1]
print(solve(B) - solve(str(int(A)-1)))
