import math
N, K = map(int, input().split())
tmp = math.ceil(N / 2)
if tmp >= K:
    print("YES")
else:
    print("NO")