# ARC037
INF = 10 ** 10
# 入力
N, M = map(int, input().split())
# Graphの作成
graph = [[] * N for _ in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)
##print(graph)

def dfs(Now, Prev):
    global flag
    # 今いる頂点からいける頂点を順に Next に入れてループ
    for Next in graph[Now]:
        if Next != Prev:
            if memo[Next]:
                # 過去に訪れていれば閉路
                flag = False
            else:
                memo[Next] = True
                dfs(Next, Now)

# 訪れたことがあるか
memo = [False for i in range(N)]

ans = 0
# 頂点をループ
for i in range(N):
    if memo[i]:     # 探索済みならスルー
        continue
    flag = True
    dfs(i, INF)      # iが未探索ならiを始点としたDFSを行う．INFは絶対に異なるということで用いる
    if flag:
        # 閉路がなければ
        ans += 1

print(ans)