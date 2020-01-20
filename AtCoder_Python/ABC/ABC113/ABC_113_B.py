# ABC113B
N = int(input())
T, A = map(int, input().split())

H = list(map(int, input().split()))

best_near = 100000000
ans = 0
for i in range(N):
    temp = T - H[i]*0.006
    if best_near > abs(A - temp):
        best_near = abs(A - temp)
        ans = i+1
print(ans)
