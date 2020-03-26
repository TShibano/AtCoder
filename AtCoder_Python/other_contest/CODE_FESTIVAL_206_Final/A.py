# A
al=[chr(ord('A') + i) for i in range(26)]

H, W = map(int, input().split())
S = [list(map(str, input().split())) for _ in range(H)]
h = 0
w = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "snuke":
            h = i
            w = j

ans = al[w] + str(h+1)
print(ans)