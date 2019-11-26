# AGC033A
# http://drken1215.hatenablog.com/entry/2019/05/05/223200
# を参考に解いた
# 多点スタートと考えて解く

from collections import deque
# 入力
H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]

# 4方向を定義
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# BFSのためのデータ構造
dist = [[-1] * W for _ in range(H)]
que_x = deque()     # H
que_y = deque()     # W

# 多点スタート地点を決める
# スタート地点は0とする
for i in range(H):
    for k in range(W):
        if field[i][k] == "#":
            dist[i][k] = 0
            que_x.append(i)
            que_y.append(k)

# 多点スタート
# 0のところから順に1を増やしていく
# ex): 3地点a, b, cからスタートとすると
# aから周囲4箇所に1をつける -> bから周囲4箇所に1をつける -> cから周囲4箇所に1をつける
# aの周囲4箇所の内1点から周囲4箇所に2をつける -> aの周囲4箇所の内2点目から周囲4箇所に2をつける
# aの周囲4箇所が終われば次はbの周囲4箇所，それが終わればcの周囲4箇所
while que_x and que_y:
    x = que_x[0]
    y = que_y[0]
    que_x.popleft()
    que_y.popleft()
    for direct in range(4):
        nx = x + dx[direct]
        ny = y + dy[direct]
        if nx < 0 or H <= nx or ny < 0 or W <= ny:      # 場外はスルー
            continue
        if dist[nx][ny] == -1:      # まだ見ていない時
            que_x.append(nx)
            que_y.append(ny)
            dist[nx][ny] = dist[x][y] + 1       # 距離の更新

# distの最大値が答え (= 最も遠いところ)
tmp = [0] * H
for i in range(H):
    tmp[i] = max(dist[i])

print(max(tmp))
