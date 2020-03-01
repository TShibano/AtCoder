# C
N, K, S = map(int, input().split())

A = [0] * N
for i in range(N):
    if i < K:
        A[i] = S
    else:
        if S == 10 ** 9:
            A[i] = 1
        else:
            A[i] = 10 ** 9

print(" ".join(map(str, A)))
