# ABC152E
# 最小公倍数
from fractions import gcd
from functools import reduce
def lcm (x, y):
    return (x * y) // gcd(x, y)

# 最小公倍数(リスト)
def lcm_list(numbers):
    return reduce(lcm, numbers, 1)

mod = 10 ** 9 + 7
N = int(input())
A = list(map(int, input().split()))

lcm_A = lcm_list(A)

ans = 0
for i in range(N):
    ans += lcm_A // A[i]

print(ans % mod)
