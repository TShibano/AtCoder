# ABC051B
K, S = map(int, input().split())
ans = 0
for i in range(K+1):
    for l in range(K+1):
        Z = S - i - l
        if Z >= 0 and Z <= K:
            ans += 1
print(ans)