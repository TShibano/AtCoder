# ABC070D
# 方針：x[i] -> K + K -> y[i]と分割できる
# 頂点 K から全ての頂点への距離を前もって求めてそれぞれのクエリを計算する．
# 各頂点への距離は BFS or DFS で実装

# BFS で実装
from collections import deque
N = int(input())
graph = [[] * N for _ in range(N)]
for i in range(N-1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append([b, c])
    graph[b].append([a, c])
    
Q, K = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(Q)]

# BFSのためのデータ構造
dist = [-1 for _ in range(N)]   # 全頂点を未訪問に
que = deque()

# 初期条件(頂点 K-1 を初期ノードとする)
dist[K-1] = 0
que.append(K-1)

# BFS 開始(キューが空になるまで探索を行う)
while que:
    v = que[0]
    que.popleft()
    for new_v_list in graph[v]:
        new_v = new_v_list[0]
        if dist[new_v] != -1:   # すでに探索済みの頂点は探索しない
            continue
        # 新たな頂点 new_vについて距離情報を更新してキューに追加する
        dist[new_v] = dist[v] + new_v_list[1]
        que.append(new_v)


for i in range(Q):
    print(dist[xy[i][0] - 1] + dist[xy[i][1] - 1])


# DFSで実装する
import sys
sys.setrecursionlimit(10 ** 8)
N = int(input())
graph = [[] * N for _ in range(N)]
for i in range(N-1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append([b, c])
    graph[b].append([a, c])
    
Q, K = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(Q)]

depth = [0] * N
def dfs(v, p, d):
    depth[v] = d
    for new_v_list in graph[v]:
        new_v = new_v_list[0]
        if new_v == p:
            continue
        dfs(new_v, v, d + new_v_list[1])

dfs(K-1, -1, 0)
for i in range(Q):
    print(depth[xy[i][0] - 1] + depth[xy[i][1] - 1])