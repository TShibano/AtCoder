# ABC117D
# 方針：各桁毎に考えて1が多ければ0に0が多ければ1にする
# X <= Kの扱い方 
# XとKのビットが初めて一致しなかった桁がdとした時
# dより上位の桁については，XはKと一致
# d桁目についてはXは0でKは1
# dより下位の桁についてはXはなんでも良い
# dを全探索する

N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

for d in range(40, -2, -1):
    if d != -1 and not (K & 1 << d):
        continue
    tmp = 0

    for e in range(40, -1, -1):
        mask = 1 << e
        num_1 = 0
        for i in range(N):
            if A[i] & mask:
                num_1 += 1
        
        if e > d:       # dより上位桁はXとKが一致
            if K & mask:
                tmp += mask * (N - num_1)
            else:
                tmp += mask * num_1
        elif e == d:    # d桁目はXは0でKは1
            tmp += mask * num_1
        else:           # dより下位桁についてはXはなんでも良い．
            tmp += mask * max(num_1, N - num_1)
    
    ans = max(ans, tmp)

print(ans)

# 以下，DPによる解法
N, K = map(int, input().split())
A = list(map(int, input().split()))
# dp[d][smaller] := 上からi番目を決定した時の最大値
# smaller: 1は次の桁はなんでも良い．0は次の桁がはK以下になるようにする．
dp = [[0] * 2 for _ in range(42)]

for d in range(1, 42):
    if dp[d-1][1] == 1:
        dp[d][1] = 1

    # Aの内，上からd桁目が1の個数を数える
    mask = 1 << (41 - d)    # 上からd桁目のbit    
    num_1 = 0               # Aの内，上からd桁目が1である数
    for i in range(N):      # num_1を数える
        if A[i] & mask:
            num_1 += 1

    if num_1 >= N - num_1:      # 上からd桁目は0にする．0は自由に選べる(1は自由に選べない)ので，1の数だけXOR計算をする
        dp[d][0] = dp[d-1][0] + num_1 * (2 ** (41-d))
        if K & mask:            # Kの上からd桁目が1の時，次の桁以降は自由に選べる
            dp[d][1] = 1
    else:                       # i桁目は1にする方が良い
        if dp[d][1]:            # 0と1を自由に選べるので1を選ぶ．つまり0の数だけXOR計算をする
            dp[d][0] = dp[d-1][0] + (N - num_1) * (2 ** (41 - d))
        else:
            if K & mask:        # Kのi桁目が1なのでi桁目は1に出来る．1を選べる．つまり0の数だけXOR計算をする
                dp[d][0] = dp[d-1][0] + (N - num_1) * (2 ** (41 - d))
            else:               # i桁目は1に出来ないので0を選ぶ．つまり1の数だけXOR計算をする
                dp[d][0] = dp[d-1][0] + num_1 * (2 ** (41 - d))

print(dp[-1][0])