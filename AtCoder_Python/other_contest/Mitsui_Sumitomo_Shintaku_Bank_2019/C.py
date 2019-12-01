X = int(input())
N = X // 100
if N * 5 >= X - N * 100:
    print(1)
else:
    print(0)
