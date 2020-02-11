# ABC138D
from collections import deque
N, Q = map(int, input().split())
Graph = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Graph[a].append(b)
    Graph[b].append(a)

counter_list = [0] * N
for i in range(Q):
    p, x = map(int, input().split())
    p -= 1
    counter_list[p] += x

# 各頂点に counter を持たせて，幅優先探索で足していく
dist = [-1 for _ in range(N)]
dist[0] = 1
que = deque()
que.append(0)
while que:
    v = que[0]
    que.popleft()
    for new_v in Graph[v]:
        if dist[new_v] != -1:
            continue
        dist[new_v] = 1
        que.append(new_v)
        counter_list[new_v] += counter_list[v]

print(" ".join(map(str, counter_list)))