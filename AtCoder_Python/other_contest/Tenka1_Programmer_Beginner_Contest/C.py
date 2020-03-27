# C
import math
N = int(input())
flag = False
for h in range(1, 3501, 1):
    for n in range(1, 3501, 1):
        bumbo = 4 * h * n - N * h - N * n
        bunshi = N * h * n
        if bumbo == 0:
            continue
        wc = math.ceil(bunshi / bumbo)
        wf = math.floor(bunshi / bumbo)
        if wc == wf and wc >= 1:
            ans_h = h
            ans_n = n
            ans_w = wc
            flag = True
            break
    if flag:
        break
print(ans_h, ans_n, ans_w)