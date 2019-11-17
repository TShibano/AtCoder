# ABC142D
import fractions
def prime_factorization(N):
    tmp = N
    ans = []
    for i in range(2, int(N ** 0.5) + 1):
        count = 0
        while tmp % i == 0:
            tmp //= i
            count += 1
        if count != 0:
            ans.append([i, count])
    if tmp != 1:
        ans.append([tmp, 1])
    if ans == []:
        ans.append([N, 1])
    return ans

A, B = map(int, input().split())

gcdAB = fractions.gcd(A, B)

if gcdAB == 1:
    print(1)
else:
    print(len(prime_factorization(gcdAB)) + 1)