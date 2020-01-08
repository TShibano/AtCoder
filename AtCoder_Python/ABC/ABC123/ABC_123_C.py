# ABC123C
import math
N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

X = min(A, B, C, D, E)
print(math.ceil(N / X) + 4)