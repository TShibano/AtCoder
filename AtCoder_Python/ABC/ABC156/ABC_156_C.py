# ABC156C
e = 0.0001
N = int(input())
X = list(map(int, input().split()))
ave = sum(X) / N
loc = round(ave + e)
ans = 0
for i in range(N):
    ans += (X[i] - loc) ** 2
print(ans)