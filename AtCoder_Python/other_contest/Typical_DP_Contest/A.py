# TypicalDPContest-A
# 方針：部分和問題に帰着し，0 ~ max値までを作れるかを調べる．
# そしてその数を調べる
N = int(input())
p = list(map(int, input().split()))

max_value = N * max(p)

# DPテーブル
dp = [[False] * (max_value + 10) for _ in range(N+10)]

dp[0][0] = True
for i in range(N):
    for j in range(max_value+1):
        if j >= p[i]:
            dp[i+1][j] = dp[i][j - p[i]] or dp[i][j]
        else:
            dp[i+1][j] = dp[i][j]

ans = 0
for j in range(0, max_value+1):
    if dp[N][j]:
        ans += 1

print(ans)


"""
他人の解答-1
setをうまく使う

ans = [0]
for p_value in p:
    ans = list(set(ans + [a + p_value for a in ans]))
print(len(ans))
"""

"""
他人の解答-2
X = sum(p)
dp = [[0] * (X + 1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(X + 1):
        # i番目の問題まででj点が作れるならdp[i][j] = 1
        if dp[i][j] == 1:
            dp[i+1][j] = 1  # ここでi番目の時の情報がi+1番目に引き継がれる
            dp[i+1][j+p[i]] = 1

print(sum(dp[-1]))
"""