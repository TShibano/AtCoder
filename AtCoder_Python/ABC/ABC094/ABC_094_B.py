# ABC094B
N, M, X = map(int, input().split())
A = list(map(int, input().split()))
count_l = 0
count_r = 0
for i in A:
    if i <= X:
        count_l += 1
    elif i >= X:
        count_r += 1
print(min(count_l, count_r))
