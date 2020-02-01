# ABC121B
N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

ans = 0
for i in range(N):
    tmp = 0
    for k in range(M):
        tmp += A[i][k] * B[k]
    if tmp > - C:
        ans += 1
print(ans)
