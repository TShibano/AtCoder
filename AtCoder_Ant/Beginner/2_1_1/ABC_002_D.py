# ABC002D
N, M = map(int, input().split())

# 関係性をTrue/Falseでつける
relation = [[False] * N for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    relation[a-1][b-1] = relation[b-1][a-1] = True

ans = 0
# 派閥を作る
# 例：i = 6 -> 0000 0000 0110 -> 2と3で派閥を作る．
for i in range(1, 2 ** N):      
    cnt = 0
    x = True
    for j in range(N):      # iの桁が1かどうかを確認する
        if (i >> j) & 1:
            cnt += 1
    if cnt <= ans:          # カウントし終えた時点でans以下なら次のiを試す
        continue
    for j in range(N):      # 関係性があるかどうかを調べる
        if (i >> j) & 1:    # 以降議員jについて関係性がある人を調べる
            for k in range(j + 1, N):       # 議員j+1, j+2, ... Nまで調べる
                if (i >> k) & 1 :           # jとk番目に関係性がある時
                    if not relation[j][k]:  # jとkに関係性が一つでもない時はFalse
                        x = False
    if x:
        ans = cnt
print(ans)