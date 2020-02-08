# ABC126C
import math
N, K =map(int, input().split())
#確率
p = []
for i in range(1, N+1):
    if i < K:
        #print(i)
        a = math.ceil((math.log2(K/i)))
        #print(a)
        p.append((0.5**a)/N)
        #print(p)
    if i >= K:
        p.append(1/N)
        #print(p)
print(sum(p))
