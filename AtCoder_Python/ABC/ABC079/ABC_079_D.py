# ABC079D
def Warshall_Floyd(V, d):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


H, W = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range(10)]
field = [list(map(int, input().split())) for _ in range(H)]

cost_list = Warshall_Floyd(10, cost)
ans = 0

for h in range(H):
    for w in range(W):
        if abs(field[h][w]) == 1:
            continue
        ans += cost_list[field[h][w]][1]

print(ans)