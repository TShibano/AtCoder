# TypicalDPContest C
# 方針：確率の問題．
# DP[r][i] := ラウンドr+1において人iが勝つ確率
# DP[r][i] = sum(自分がそのラウンドまで勝ち上がる確率 * 相手がそのラウンドまで勝ち上がる確率 * 自分がその相手と戦って勝つ確率)
# 相手はラウンドに合わせて変化する．ここをどう実装するかが鍵か？

# 入力
K = int(input())
R = [int(input()) for _ in range(2**K)]

# 勝率の関数
def prob(winner, loser):
    return 1 / (1 + 10 ** ((R[loser] - R[winner]) / 400))

# dpテーブル
dp = [[0] * (2**K) for _ in range(K)]

# dpテーブルの初期条件(ラウンド1の勝率)
for i in range(0, 2**K, 2):
    dp[0][i] = prob(i, i+1)
    dp[0][i+1] = prob(i+1, i)

# ラウンド2  ~ K(r = 1 ~ K-1)までを考える
for r in range(1, K):
    i = 0   # 人(0 ~ 2 ** K - 1)
    # ex) 8人でラウンド2なら(0, 1) vs (2, 3), (4, 5) vs (6, 7)の2つの塊(battle_set)を考える
    # (0, 1) vs (2, 3)に着目すると前半(Small)と後半(Large)がある．
    # (4, 5) vs (6, 7)も同様．前半後半を分けるのがinter_flag．
    battle_set = 0      
    inter_flag = "S"

    while battle_set < 2 ** (K - r - 1):        # battle_setの個数は 2 ** (K - r - 1) = (2 ** K / 2 ** (r+1))
        if i == 2 ** K:     # 2 ** K番目の人はいない
            break
        if i != 0 and i % (2 ** (r+1)) == 0:    # 2 ** (r+1)番目の人は次のbattle_setになる
            battle_set += 1
        cnt = 0     # i番目の人が戦わなければならない人数
        tmp_small = (2 ** (r+1)) * (battle_set)     # 後半グループのi番目の人が戦い始める人
        tmp_large = tmp_small +  2 ** r             # 前半グループのi番目の人が戦い始める人
        # debug : print(r, i, battle_set,  tmp_large, tmp_small)
        if inter_flag == "S":       # 前半グループ
            while cnt < 2 ** r:     # 闘う人数は2 ** (r+1) / 2  (= ラウンド数の二乗の半分)
                dp[r][i] += dp[r-1][i] * dp[r-1][tmp_large + cnt] * prob(i, tmp_large + cnt)
                cnt += 1
            if (i + 1) % (2 ** r) == 0:     # 前半グループの終わり
                inter_flag = "L"
                i += 1
                continue
            else:                           # 前半グループの途中
                i += 1
                continue
        if inter_flag == "L":       # 後半グループ．前半グループと同じ．闘う相手が変わっただけ
            while cnt < 2 ** (r):
                dp[r][i] += dp[r-1][i] * dp[r-1][tmp_small + cnt] * prob(i, tmp_small + cnt)
                cnt += 1
            if (i + 1) % (2 ** r) == 0:
                inter_flag = "S"
                i += 1
                continue
            else:
                i += 1
                continue

# 答えを出力
for i in range(2**K):
    print("{:.10f}".format(dp[K-1][i]))