# ABC130B
N, X = map(int, input().split())
L = list(map(int, input().split()))
D = 0
for i in range(1, N+1):
    D += L[i-1]
    # print(i+1, D)
    if D > X:
        ans = i
        break
    if i == N:
        ans = i+1

print(ans)
