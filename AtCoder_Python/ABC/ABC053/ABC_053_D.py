# ABC053D
import collections

N = int(input())
A = list(map(int, input().split()))
a = collections.Counter(A)
a = a.most_common()
cnt = 0
for i in range(len(a)):
    if a[i][1] % 2 == 0:
        cnt += 1
if cnt % 2 == 0:
    print(len(a))
else:
    print(len(a) - 1)
