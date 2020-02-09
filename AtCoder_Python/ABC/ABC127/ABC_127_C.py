# ABC127C
N, M = map(int, input().split())
lr = []
for i in range(M):
    lr.append(list(map(int, input().split())))
l = lr[0][0]
r = lr[0][1]
for i in range(1, M):
    if lr[i][0] > l:
        l = lr[i][0]
    if lr[i][1] < r:
        r = lr[i][1]
    
if r >= l:
    print(r - l + 1)
else:
    print(0)
