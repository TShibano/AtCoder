# B
K, T = map(int, input().split())
A = list(map(int, input().split()))
res = K - max(A)
a = max(A)
if T == 1:
    print(K - 1)
    exit()
if res >= a + 1:
    print(0)
    exit()

ans = a - 1
ans -= res
print(ans)