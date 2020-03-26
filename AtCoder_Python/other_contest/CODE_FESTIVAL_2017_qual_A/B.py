# B
N, M, K = map(int, input().split())
ans = "No"
for h in range(0, N+1, 1):
    for w in range(0, M+1, 1):
        tmp = h * M + w * N - 2*h*w
        if tmp == K:
            ans = "Yes"
            print(ans)
            exit()
print(ans)