# ABC070C
# ABC070-C
import fractions
from functools import reduce
N = int(input())
T = []
for i in range(N):
    T.append(int(input()))

def lcm_base(x, y):
    return (x * y ) // fractions.gcd(x, y)
def lcm_list(numbers):
    return reduce(lcm_base, numbers)
print(lcm_list(T))
