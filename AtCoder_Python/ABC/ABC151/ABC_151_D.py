# ABC151D
from collections import deque
H, W = map(int, input().split())
field = [input() for _ in range(H)]
ans = 0

# 4方向の移動
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


for h in range(H):
    for w in range(W):
        # BFSのためのデータ構造
        if field[h][w] == "#":
            continue
        dist = [[-1] * W for _ in range(H)]
        que_x = deque()
        que_y = deque()
        dist[h][w] = 0
        que_x.append(h)
        que_y.append(w)

        # BFS開始
        while que_x and que_y:
            x = que_x[0]
            y = que_y[0]
            que_x.popleft()
            que_y.popleft()
            tmp_max = 0
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
        for i in range(H):
            for k in range(W):
                tmp_max = max(dist[i][k], tmp_max)
        ans = max(tmp_max, ans)
print(ans)
