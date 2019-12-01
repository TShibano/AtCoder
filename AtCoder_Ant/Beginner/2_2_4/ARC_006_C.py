# ARC006C
# 後ろから貪欲
# 上から下に置いていく
# 一番下の箱の重さのリストを作成し，下に入れられるところから入れていく
N = int(input())
w = [int(input()) for _ in range(N)]

under_box_list = [w[N-1]]
for i in range(N-2, -1, -1):
    k = 0   # under_box_listを走査するためのインデクス
    while 1:
        if w[i] >= under_box_list[k]:   # 今の箱が重い時，下に加える
            under_box_list[k] = w[i]
            break
        if k == len(under_box_list) - 1:    # 下における箱がない時は，新しいところにおく
            under_box_list.append(w[i])
            break
        k += 1

print(len(under_box_list))


'''
# 方針：前から貪欲
# 今段ボールの一番上のみのリストを作成し，乗せられるところに乗せていく
# その際は上が一番軽いところから乗せていく
N = int(input())
w = [int(input()) for _ in range(N)]

top_box_list = [w[0]]
for i in range(1, N):
    k = 0   # top_box_listを走査するためのインデクス
    under_box_list.sort()   # ソートすることでk = 0, 1, 2, でも小さいところから見れる
    while 1:
        if w[i] <= under_box_list[k]:
            under_box_list[k] = w[i]
            break
        if k == len(under_box_list) - 1:
            under_box_list.append(w[i])
            break
        k += 1

print(len(top_box_list))
'''