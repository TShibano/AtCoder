# ABC007C
from collections import deque
# 入力
R, C = map(int, input().split())
s_x, s_y = map(int, input().split())
g_x, g_y = map(int, input().split())
s_x -= 1
s_y -= 1
g_x -= 1
g_y -= 1

# get filed map
field = [list(input()) for _ in range(R)]

# 4方向の移動
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# BFSのためのデータ構造
dist = [[-1] * C for i in range(R)]
que_x = deque()
que_y = deque()

# 初期条件(スタート地点を0にする)
dist[s_x][s_y] = 0  
que_x.append(s_x)
que_y.append(s_y)

# BFS 開始
while que_x and que_y:
    x = que_x[0]
    y = que_y[0]
    que_x.popleft()
    que_y.popleft()
    for direct in range(4):
        nx = x + dx[direct]
        ny = y + dy[direct]
        if 0 > nx or nx >= R or 0 > y or ny >= C:   # 場外はスルー
            continue
        if field[nx][ny] == "#":        # 壁はスルー
            continue
        if dist[nx][ny] == -1:      # まだ見ていない時
            que_x.append(nx)
            que_y.append(ny)
            dist[nx][ny] = dist[x][y] + 1   # 距離の更新

print(dist[g_x][g_y])