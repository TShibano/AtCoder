# ABC099C
"""
import bisect
N = int(input())
ans = 0
hikidashi_list = [1, 6, 9]
tmp_6 = 6
tmp_9 = 9
while tmp_6 < N:
    tmp_6 *= 6
    hikidashi_list.append(tmp_6)

while tmp_9 < N:
    tmp_9 *= 9
    hikidashi_list.append(tmp_9)

hikidashi_list.sort()
while N > 0:
    now = bisect.bisect_left(hikidashi_list, N)
    if now == 0:
        N -= 1
    else:
        N -= hikidashi_list[now-1]
    ans += 1
print(ans)

# 貪欲に大きいお金から取るのでは無理
# N = 13 解3 (6, 6, 1)  本法5 (9, 1, 1, 1, 1)
"""

# DP
N = int(input())
dp = [100000000] * (N+1)
dp[0] = 0
dp[1] = 1
ans = 0
hikidashi_list = [1, 6, 9]
tmp_6 = 6
tmp_9 = 9
while tmp_6 < N:
    tmp_6 *= 6
    hikidashi_list.append(tmp_6)

while tmp_9 < N:
    tmp_9 *= 9
    hikidashi_list.append(tmp_9)
hikidashi_list.sort()
for i in range(N+1):
    for k in hikidashi_list:
        if i + k > N :
            break
        dp[i+k] = min(dp[i] + 1, dp[i+k])

print(dp[N])