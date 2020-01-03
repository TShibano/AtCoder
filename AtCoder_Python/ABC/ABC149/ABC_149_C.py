# ABC149C
import math
def is_prime(N):
    if N == 1:
        return False
    for k in range(2, int(math.sqrt(N)) + 1):
        if N % k == 0:
            return False
    return True

X = int(input())
for i in range(X, 2 * 10 ** 7):
    if is_prime(i):
        print(i)
        exit()