# ABC108C
N, K = map(int, input().split())

ans = 0

if N == 1 and K != 1:
    print(0)
    exit()
if K % 2 == 0:
    # a, b, c が全て K の倍数
    cnt = N // K 
    ans = cnt ** 3
    K //= 2
    k = K
    # a, b, c が K//2 の奇数倍
    tmp = 1
    while 1:
        K += 2 * k
        if N < K:
            break
        tmp += 1
    ##print(cnt, tmp)
    ans += (tmp) ** 3
else:
    cnt = N // K
    ans = cnt ** 3

print(ans)