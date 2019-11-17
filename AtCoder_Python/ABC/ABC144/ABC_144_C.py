# ABC144C
# 素因数分解
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

N = int(input())
prime_N = prime_factorization(N)
if len(prime_N) == 1 and prime_N[0][1] == 1:
    print(N - 1)
    exit()
start = int(N ** 0.5) + 1
ans_a = 0
ans_b = 0
for a in range(start, 1, -1):
    b = N // a
    if N == a * b:
        ans_a = a
        ans_b = b
        break

print(ans_a + ans_b - 2)