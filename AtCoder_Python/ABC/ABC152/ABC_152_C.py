# ABC152C
N = int(input())
P = list(map(int, input().split()))

ans = 0
tmp_min = P[0]

for i in range(N):
    if P[i] <= tmp_min:
        ans += 1
        tmp_min = min(P[i], tmp_min)
    else:
        tmp_min = min(P[i], tmp_min)

print(ans)
