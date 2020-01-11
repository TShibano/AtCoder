# ABC077B
import math
def check(N):
    n = math.sqrt(N)
    return math.floor(n) == math.ceil(n)
N = int(input())
flag = False
for i in range(N, 0, -1):
    flag = check(i)
    if flag:
        print(i)
        break
        
# 解説
N = int(input())
for i in range(1, N+2):
    if i ** 2 > N:
        print((i - 1) ** 2)
        break
