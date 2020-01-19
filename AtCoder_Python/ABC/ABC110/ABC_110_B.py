# ABC110B
N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

flag = True

x = sorted(x)
y = sorted(y)

if Y - X < 2:
    flag = False

if y[0] <= x[-1] or (y[0] <= X or x[-1] >= Y):
    flag = False


if flag:
    print("No War")
else:
    print("War")

