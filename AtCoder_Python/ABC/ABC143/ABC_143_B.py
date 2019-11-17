# ABC143B
N = int(input())
D = list(map(int, input().split()))
ans = 0
for i in range(N-1):
    for k in range(i+1, N):
        ans += D[i] * D[k]
print(ans)