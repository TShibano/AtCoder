# ABC075C
# 使わない辺を一つづつ考える
# BFSでいけない頂点があればその使わない辺は橋

from collections import deque
N, M = map(int, input().split())
graph = [[] * N for _ in range(N)]
uv = [list(map(int, input().split())) for _ in range(M)]

ans = 0
for i in range(M):
    graph = [[] * N for _ in range(N)]
    for k in range(M):
        if k == i:
            continue
        u = uv[k][0] - 1
        v = uv[k][1] - 1
        graph[u].append(v)
        graph[v].append(u)
    
    # BFSのためのデータ構造
    dist = [False for _ in range(N)]
    que = deque()

    # 初期条件
    dist[0] = True
    que.append(0)

    # BFS開始
    while que:
        v = que[0]
        que.popleft()
        for new_v in graph[v]:
            if dist[new_v]:
                continue
            # 探索した頂点はTrueにする
            dist[new_v] = True
            que.append(new_v)
    
    if False in dist:
        ans += 1

print(ans)