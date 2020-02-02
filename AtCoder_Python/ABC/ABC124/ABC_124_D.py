# ABC124D
import math
N, K = map(int, input().split())
S = input()

# 連続した 0 と 1 の数を数える
cnt_list = []
flag = True if S[0] == '1' else False
cnt = 1
flag_flag = True
for i in range(1, N):
    if S[i] == '1':
        if i == N - 1:
            flag_flag = True
        if flag:
            cnt += 1
        else:
            flag = True
            cnt_list.append([cnt, -1])
            cnt = 1
    if S[i] == '0':
        if i == N - 1:
            flag_flag = False
        if flag:
            flag = False
            cnt_list.append([-1, cnt])
            cnt = 1
        else:
            cnt += 1
if not flag_flag:
    cnt_list.append([cnt, -1])
else:
    cnt_list.append([-1, cnt])
# 指示する回数を求める． K 回 >= 連続した 0 の個数の時は上手に行えば全て逆立ちできる
n = len(cnt_list)
if cnt_list[0][0] == -1:    # 1 スタート
    if K >= n//2:
        print(N)
        exit()
    k = K
else:                       # 0 スタート
    if K >= math.ceil(n/2):
        print(N)
        exit()
    k = K

# あとは区間内の総和を計算するのに累積和を用いる
# 累積和を計算
cumsum = [0] * (n+1)
for i in range(n):
    cumsum[i+1] = cumsum[i] + max(cnt_list[i])

ans = 0
if cnt_list[0][0] == -1:        # 1 start
    if cnt_list[-1][0] == -1:   # 1 end
        for i in range(1, n - 2 * k + 1, 2):
            ans = max(ans, cumsum[2 * k + i] - cumsum[i-1])
    else:                        # 0 end
        for i in range(1, n - 2*k + 1, 2):
            ans = max(ans, cumsum[2 * k + i] - cumsum[i-1])
        ans = max(ans, cumsum[n] - cumsum[n - 2*k])
    
else:                           # 0 start
    if cnt_list[-1][0] == -1:   # 1 end
        ans = cumsum[2*k] - cumsum[0]
        for i in range(2, n - 2 * k + 1, 2):
            ans = max(ans, cumsum[2 * k + i] - cumsum[i-1])
    else:                       # 0 end
        ans = cumsum[2 * k] - cumsum[0]
        for i in range(2, n - 2 * k + 1, 2):
            ans = max(ans, cumsum[ 2* k + i] - cumsum[i-1])
        ans = max(ans, cumsum[n] - cumsum[n - 2*k])
##print(cumsum)
print(ans)