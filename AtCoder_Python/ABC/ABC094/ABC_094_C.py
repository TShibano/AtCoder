# ABC094C
N = int(input())
X = list(map(int, input().split()))
Y = sorted(X)
left_median = Y[N // 2 - 1]
right_megian = Y[N // 2]
if left_median == right_megian:
    for i in range(N):
        print(left_median)
else:
    for i in X:
        if i > left_median:
            print(left_median)
        else:
            print(right_megian)
