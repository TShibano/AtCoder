# ABC052D
# ABC052D
N, A, B = map(int, input().split())
X = list(map(int, input().split()))
ans = 0
thres = B // A
for i in range(N-1):
    x = X[i+1] - X[i]
    if x > thres:
        ans += B
    else:
        ans += A * x
print(ans)
