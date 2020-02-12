# ABC140C
N = int(input())
B = list(map(int, input().split()))

A = [0] * N
A[N-1] = B[N-2]
for i in range(N-2, 0, -1):
    A[i] = min(B[i], B[i-1])

A[0] = B[0]
print(sum(A))