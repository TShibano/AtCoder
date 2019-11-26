# ABC088
# 最短経路問題になる
from collections import deque
import copy
# 入力
H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]
field_original = copy.deepcopy(field)

# 4方向の移動
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# BFSのためのデータ構造
dist = [[-1] * W for _ in range(H)]
que_x = deque()
que_y = deque()

# 探索中に各マスはどこからきたのかを表す配列
prev_x = [[-1] * W for _ in range(H)]
prev_y = [[-1] * W for _ in range(H)]

# 初期条件(スタート地点を0にする)
dist[0][0] = 0
que_x.append(0)
que_y.append(0)

# BFS開始
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
        if field[nx][ny] == "#":     # 壁はスルー
            continue
        if dist[nx][ny] == -1:          # まだ見ていない時
            que_x.append(nx)
            que_y.append(ny)
            dist[nx][ny] = dist[x][y] + 1   # 距離の更新
            prev_x[nx][ny] = x      # どの頂点から伝播してきたかを 縦 方向の座標をメモ
            prev_y[nx][ny] = y      # どの頂点から伝播してきたかを 横 方向の座標をメモ

x = H - 1
y = W - 1

if dist[x][y] == -1:        # ゴール出来てない時は -1 で終了
    print(-1)
    exit()
##print(dist[H-1][W-1])
while x != -1 and y != -1:
    field[x][y] = "o"

    # 前の頂点へいく
    px = prev_x[x][y]
    py = prev_y[x][y]
    x, y = px, py
##print(field)
ans = 0
for i in range(H):
    for k in range(W):
        if field[i][k] == field_original[i][k] == ".":
            ans += 1
print(ans)