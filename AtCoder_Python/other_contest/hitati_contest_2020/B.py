# B
a, b, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
xyc = [list(map(int, input().split())) for _ in range(m)]
tmp = min(A) + min(B)
tmp1 = 100000000
for i in range(m):
    aa = xyc[i][0] - 1
    bb = xyc[i][1] - 1
    tmp1 = min(A[aa] + B[bb] - xyc[i][2], tmp1)

print(min(tmp, tmp1))