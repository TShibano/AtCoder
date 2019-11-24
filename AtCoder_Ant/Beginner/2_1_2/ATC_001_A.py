# ATC001A
import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, H, W, meiro):
    # 迷路の外側を指定した時
    if x < 0 or x >= H:
        return False
    if y < 0 or y >= W:
        return False
    # 壁だった時
    if meiro[x][y] == "#":
        return False
    
    # すでに行ったことがある時
    if meiro[x][y] == "q":
        return False
    
    # ゴールを見つけた時
    if meiro[x][y] == "g":
        return True
    
    # 今いる位置へ印をつける
    meiro[x][y] = "q"

    # 周囲4マスを探索
    return dfs(x-1, y, H, W, meiro) or dfs(x+1, y, H, W, meiro) or dfs(x, y-1, H, W, meiro) or dfs(x, y+1, H, W, meiro)

def main():
    H, W = map(int, input().split())
    meiro = [list(input()) for _ in range(H)]
    for i in range(H):
        for k in range(W):
            if meiro[i][k] == "s":
                a, b = i, k
    print("Yes") if dfs(a, b, H, W, meiro) else print("No")

if __name__ == "__main__":
    main()
