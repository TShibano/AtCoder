# ABC080C
N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

ans_list = [0] * (2 ** 10 - 1)
# 開ける時間をbit全探索
for i in range(1, 2**10):
    open_day = [0] * 10
    # 店を開ける時間を調べる
    for j in range(10):
        if i & (1 << j):
            open_day[j] = 1
    # 店k について一緒に開く時間帯の数を調べ，その個数をP[k][count]に入れる
    for k in range(N):
        count = 0
        for t in range(10):
            if open_day[t] == F[k][t] and F[k][t] == 1:
                count += 1
        ans_list[i-1] += P[k][count]

print(max(ans_list))