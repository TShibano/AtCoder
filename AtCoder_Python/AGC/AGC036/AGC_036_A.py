# AGC036A
# 解説見た
# (0, 0), (10**9, 1), (X3, Y3)で考える
# 10**9 * Y3 = S + X3
S = int(input())
M = 10 ** 9
X1 = 0
Y1 = 0
X2 = M
Y2 = 1
X3 = (M - S%M)%M        # 具体的に書いてみれば分かる
Y3 = (S + X3) // M
print(X1, Y1, X2, Y2, X3, Y3)

'''
以下間違い
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

S = int(input())
if S <= 10 ** 9:
    print(0, 0, 0, 1, S, 0)
    exit()
if S == 10 ** 18:
    print(0, 0, 0, 10**9, 10**9, 0)
    exit()

keta = [int(c) for c in str(S)]
N = len(keta)
X3 = 0
for i in range(9):
    X3 += keta[i] * 10 ** (8-i)
Y2 = 10 ** (N - 9)

res = S - X3*Y2
X2 = res
Y3 = 1
print(0, 0, X2, Y2, X3, Y3)

'''