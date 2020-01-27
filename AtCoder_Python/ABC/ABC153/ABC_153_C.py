# ABC153C
N, K = map(int, input().split())
H = list(map(int, input().split()))

H.sort(reverse = True)
ans = 0 
for i in range(K, N, 1):
    ans += H[i]
print(ans)
