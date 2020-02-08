# ABC125D
N = int(input())
A = list(map(int, input().split()))

cnt_minus = 0
wa = 0
small = 10 ** 10
for i in range(N):
    if A[i] < 0:
        cnt_minus += 1
    wa += abs(A[i])
    small = min(abs(A[i]), small)
    

if cnt_minus % 2 == 0:
    print(wa)
else:
    print(wa - (2 * small))