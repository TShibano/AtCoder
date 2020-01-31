# ABC112D
def is_prime(N):
    if N == 1:
        return False
    for k in range(2, int(N**0.5) + 1):
        if N % k == 0:
            return False
    return True


N, M = map(int, input().split())
k = 0
if N != 1:
    if is_prime(M):
        print(1)
        exit()
while True:
    if M % (N + k) == 0:
        ans = M // (N+k)
        break
    k += 1
print(ans)


# 解説
# a[i] (i = 0, ... , N-1) の最大公約数をDとしたとき，M も D で割り切れる
# よって D は M の約数
# M の約数かつ(M//N)以下の整数の中で最大のものが答え
import bisect
def make_divisors(N):
    divisors = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            divisors.append(i)
            if i != N // i:
                divisors.append(N//i)
    divisors.sort()
    return divisors
N, M = map(int, input().split())
lst = make_divisors(M)
print(lst[bisect.bisect_right(lst, M//N)-1])