# ABC094D
import bisect
N = int(input())
A = list(map(int, input().split()))

A.sort()
i = A[-1]
middle = i/2
j_right = bisect.bisect_right(A, middle)
left = A[j_right - 1]
right = A[j_right]
if abs(middle - left) <= abs(middle - right):
    j = left
else:
    j = right
print(i, j)