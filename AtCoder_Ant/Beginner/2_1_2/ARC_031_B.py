# ARC031B
# 他人のコードをみた
# 細かいところを間違っていた
# 方針：
# 一つ埋めるところを全探索して，埋めたfield上の島の数ををDFSで数え上げる
# 数え上げた島の数が1なら答え

import sys
import copy
sys.setrecursionlimit(10 ** 8)

H, W = 10, 10
field = [list(input()) for _ in range(H)]
# 4方向の移動
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def dfs(x, y):
    now_field[x][y] = "x"
    # 4方向を探索
    for direct in range(4):
        nx = x + dx[direct]
        ny = y + dy[direct]

        # 次行くところが場外もしくは海だったら
        if nx < 0 or nx >= H or ny < 0 or ny >= W:
            continue
        if now_field[nx][ny] == "x":
            continue
        
        # 再帰探索
        dfs(nx, ny)

for i in range(H):
    for k in range(W):
        now_field = copy.deepcopy(field)
        now_field[i][k] = "o"
        cnt = 0

        for h in range(H):
            for w in range(W):
                if now_field[h][w] == "x":
                    continue
                dfs(h, w)
                cnt += 1
        if cnt == 1:
            print("YES")
            exit()
print("NO")