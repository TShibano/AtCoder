# ARC005C
# 0-1BFS
# 道は0，壁への移動を1として考える
# 次が壁なら末尾に入れて，次が道なら先頭に入れる
# 先頭から取り出す
# ゴールにたどり着くまでに通った壁の個数を数える

from collections import deque
# 入力
H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]

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


# スタートとゴール
for i in range(H):
    for k in range(W):
        if field[i][k] == "s":
            s_x = i
            s_y = k
        if field[i][k] == "g":
            g_x = i
            g_y = k

# 初期条件
dist[s_x][s_y] = 0
que_x.append(s_x)
que_y.append(s_y)


# BFS開始
while que_x and que_y:
    x = que_x[0]
    y = que_y[0]
    que_x.popleft()
    que_y.popleft()
    for direct in range(4):
        nx = x + dx[direct]
        ny = y + dy[direct]
        if nx < 0 or H <= nx or ny < 0 or W <= ny:
            continue
        if dist[nx][ny] != -1:
            continue
        if field[nx][ny] == "#":
            dist[nx][ny] = 1
            que_x.append(nx)
            que_y.append(ny)
            prev_x[nx][ny] = x
            prev_y[nx][ny] = y
        else:
            dist[nx][ny] = 0
            que_x.appendleft(nx)
            que_y.appendleft(ny)
            prev_x[nx][ny] = x
            prev_y[nx][ny] = y

x = g_x
y = g_y
cnt = 0

while x != -1 and y != -1:
    if field[x][y] == "#":
        cnt += 1
    px = prev_x[x][y]
    py = prev_y[x][y]
    x, y = px, py

##print(cnt)
if 0 <= cnt <= 2:
    print("YES")
else:
    print("NO")