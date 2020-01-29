# ABC109C
import fractions
from functools import reduce
def gcd_list(lst):
    return reduce(fractions.gcd, lst)

N, X = map(int, input().split())
x = list(map(int, input().split()))
x.append(X)
x.sort()

diff_list = [0] * (N)
for i in range(N):
    diff_list[i] = x[i+1] - x[i]


ans = gcd_list(diff_list)
print(ans)
