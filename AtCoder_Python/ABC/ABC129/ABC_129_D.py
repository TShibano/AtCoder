# ABC129D
H, W = map(int, input().split())
field = [input() for _ in range(H)]

# Left
Left = [[0] * W for _ in range(H)]
for h in range(H):
    cnt = 0
    for w in range(W):
        if field[h][w] == '#':
            cnt = 0
        else:
            cnt += 1
        Left[h][w] = cnt

# Right
Right = [[0] * W for _ in range(H)]
for h in range(H):
    cnt = 0
    for w in range(W-1, -1, -1):
        if field[h][w] == '#':
            cnt = 0
        else:
            cnt += 1
        Right[h][w] = cnt

# Up
Up = [[0] * W for _ in range(H)]
for w in range(W):
    cnt = 0
    for h in range(H):
        if field[h][w] == '#':
            cnt = 0
        else:
            cnt += 1
        Up[h][w] = cnt

# Down
Down = [[0] * W for _ in range(H)]
for w in range(W):
    cnt = 0
    for h in range(H-1, -1, -1):
        if field[h][w] == '#':
            cnt = 0
        else:
            cnt += 1
        Down[h][w] = cnt

# 集計
ans = -1
for h in range(H):
    for w in range(W):
        ans = max(ans, Left[h][w] + Right[h][w] + Up[h][w] + Down[h][w] - 3)
print(ans)

