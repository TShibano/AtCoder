# ABC154D
N, K = map(int, input().split())
P = list(map(int, input().split()))

wa = sum(P[:K])
tmp = wa
ind = 0
for i in range(1, N - K+1, 1):
    tmp +=P[i+K-1]
    tmp -= P[i-1]
    if tmp > wa:
        wa = tmp
        ind = i
    else:
        pass

# 期待値を求める
ans = 0

for i in range(ind, ind+K, 1):
    now = P[i]
    ans += (now+1) /2
print("{:.10f}".format(ans))
