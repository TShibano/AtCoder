# ABC126D
from collections import deque
N = int(input())
graph = [[] * N for _ in range(N)]

for i in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append([v, w])
    graph[v].append([u, w])

dist = [-1 for _ in range(N)]
que = deque()
dist[0] = 0
que.append(0)

while que:
    v = que[0]
    que.popleft()
    for i in range(len(graph[v])):
        nv = graph[v][i][0]
        d = graph[v][i][1]
        if dist[nv] != -1:
            continue
        dist[nv] = dist[v] + d
        que.append(nv)

for i in range(N):
    if dist[i] % 2 == 0:
        print(0)
    else:
        print(1)