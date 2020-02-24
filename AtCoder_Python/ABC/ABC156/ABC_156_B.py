# ABC156B
N, K = map(int, input().split())
ans = 0
while N >= K ** ans:
    ans += 1
    print(ans)
print(ans)