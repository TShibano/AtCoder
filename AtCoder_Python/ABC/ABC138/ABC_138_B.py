# ABC138B
N = int(input())
A = list(map(int, input().split()))
tmp = 0
for i in range(N):
    tmp += 1 / A[i]
ans = 1 / tmp

print("{:.10f}".format(ans))