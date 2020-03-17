# A
M, D = map(int, input().split())
ans = 0
for m in range(M+1):
    for d in range(10, D+1):
        d1 = int(str(d)[0])
        d2 = int(str(d)[1])
        if d1 > 1 and d2 > 1 and m == d1 * d2:
            ans += 1
print(ans)
