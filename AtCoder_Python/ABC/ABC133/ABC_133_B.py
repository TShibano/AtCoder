# ABC133B
import math
N, D = map(int, input().split())
X = []
for i in range(N):
    X.append(list(map(int, input().split())))

ans = 0
for i in range(N-1):
    for k in range(i+1, N):
        distance = 0
        for z in range(D):
            distance += (X[i][z] - X[k][z]) ** 2
        if math.ceil(distance**0.5) == math.floor(distance**0.5):
            ans += 1
print(ans)
