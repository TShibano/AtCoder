# ABC059C
import numpy as np
N = int(input())
A = list(map(int, input().split()))

res_plus = np.cumsum(A)
res_minus = np.cumsum(A)
ans_plus = 0
ans_minus = 0

tmp_tmp = 0
# 奇数項を正とする
for i in range(N):
    res_plus[i] += tmp_tmp
    if i % 2 == 0:         # 奇数項   
        if res_plus[i] > 0:
            pass
        else:
            tmp = 1 - res_plus[i]
            ans_plus += tmp
            tmp_tmp += tmp
    else:                  # 偶数項
        if res_plus[i] < 0:
            pass
        else:
            tmp = res_plus[i] + 1
            ans_plus += tmp
            tmp_tmp -= tmp


tmp_tmp = 0
# 奇数項を負とする
for i in range(N):
    res_minus[i] += tmp_tmp
    if i % 2 == 0:      # 奇数項
        if res_minus[i] < 0:
            pass
        else:
            tmp = res_minus[i] + 1
            ans_minus += tmp
            tmp_tmp -= tmp
    else:               # 偶数項
        if res_minus[i] > 0:
            pass
        else:
            tmp = 1 - res_minus[i]
            ans_minus += tmp
            tmp_tmp += tmp

##print(ans_minus, ans_plus)
print(min(ans_plus, ans_minus))