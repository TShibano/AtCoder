# DDCC2020C
H, W, K = map(int, input().split())
S = [list(input()) for _ in range(H)]
ans_table = [[0] * W for _ in range(H)]
cnt = 1
for i in range(H):
    loc = 0
    flag = False
    for k in range(W):
        if S[i][k] == "#":
            for a in range(loc, k+1):
                ans_table[i][a] = cnt
            loc = k+1
            cnt += 1
            flag = True
        if flag:
            if k == W - 1 and S[i][k] == ".":
                for a in range(loc, W):
                    ans_table[i][a] = cnt - 1
        else:
            pass
if sum(ans_table[0]) != 0:
    for i in range(1, H):
        if sum(ans_table[i]) == 0:
            ans_table[i] = ans_table[i-1] 
if sum(ans_table[0]) == 0:
    for i in range(1, H):
        if sum(ans_table[i]) != 0:
            chech = i
            break
    for i in range(0, chech):
        ans_table[i] = ans_table[chech]
    for i in range(chech, H):
        if sum(ans_table[i]) == 0:
            ans_table[i] = ans_table[i-1]

for a in ans_table:
    print(*a)