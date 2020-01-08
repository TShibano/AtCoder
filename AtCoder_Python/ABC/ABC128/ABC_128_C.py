# ABC128C
N, M = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(M)]
p = list(map(int, input().split()))

ans = 0

# bit全探索
for i in range(2 ** N):
    switch_list = [0] * N
    flag = True     # 一つでも電球とスイッチの条件を満たさないならFalseにする
    for j in range(N):
        if i & (1 << j):    # 0 or 1 を調べるためのループ
            switch_list[j] = 1
    for k in range(M):  # 電球kについて
        on_swtich = 0
        for s in range(ks[k][0]):   # 繋がっているks[k][0]個のスイッチの状態を調べる
            if switch_list[ks[k][s+1] - 1] == 1:
                on_swtich += 1
        if on_swtich % 2 == p[k]:
            pass
        else:
            flag = False
            break
    if flag:
        ans += 1

print(ans)