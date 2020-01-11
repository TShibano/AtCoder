# ABC077C
import bisect
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()
ans = 0
for i in range(N):
    b_min = bisect.bisect_right(B, A[i])
    for k in range(b_min, N):
        c_min = bisect.bisect_right(C, B[k])
        ans += N - c_min
        ##print(i, k, ans)

print(ans)

# 以下，解説をみた
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
C.sort()
ans = 0
for b in B:
    a_max = bisect.bisect_left(A, b)
    c_min = bisect.bisect_right(C, b)
    ans += a_max * (N - c_min)
print(ans)