# ABC104C
# 解説をみた．
# 一部をとる場合は，まだ残っていてかつ最大の点数のもので良い
import math
inf = 10000000000000000
D, G = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(D)]
ans_cnt = inf
# bit全探索
# ex)i = 0b0000011111 -> 1 ~ 5問目まで全て解く
for i in range(2 ** D):
    flag = True
    tmp_score = 0           # iにおけるscore
    tmp_cnt = 0             # iにおけるcount
    for j in range(D):      # iの各桁が1かどうかを調べる
        if (i >> j) & 1:    # 1の時は足していく
            tmp_score += pc[j][0] * (100 * (j+1)) + pc[j][1]    # p[j]とボーナスを全部足す
            tmp_cnt += pc[j][0]                                 # p[j]:をcountに足す
    if tmp_score < G:       # 足りない時
        for j in range(D-1, -1, -1):    # 使っていなくてかつ最も大きいところからとってくる
            if not (i >> j) & 1:
                tmp_tmp_cnt = math.ceil((G - tmp_score) / ((j+1) * 100))        # Gを超えるのに必要な点数
                if tmp_tmp_cnt > pc[j][0]:          # もってる枚数より多い場合はダメ
                    flag = False
                    break
                else:                               # 足りるならcntに加える
                    tmp_cnt += tmp_tmp_cnt
                    break
    if flag:
        ans_cnt = min(tmp_cnt, ans_cnt)
print(ans_cnt)