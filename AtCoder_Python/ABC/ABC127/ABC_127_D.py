# ABC127D
N, M = map(int, input().split())
A = list(map(int, input().split()))
BC = [list(map(int, input().split())) for _ in range(M)]

A.sort()
BC.sort(key = lambda x:(-x[1]))

i_a = 0
i_bc = 0
while i_a < N:
    if i_bc == M:
        break
    for j in range(BC[i_bc][0]):
        if i_a + j >= N:
            i_a = N
            continue
        if A[i_a + j] >= BC[i_bc][1]:
            i_a = N
        else:
            A[i_a + j] = BC[i_bc][1]
    i_a += BC[i_bc][0]
    i_bc += 1

print(sum(A))
