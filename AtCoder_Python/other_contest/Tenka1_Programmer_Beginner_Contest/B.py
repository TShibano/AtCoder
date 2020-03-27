# B
N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b

print(max(A) + B[A.index(max(A))])
