# ABC154C
N=int(input())
A = list(map(int, input().split()))
b = list(set(A))
if len(A) == len(b):
    print("YES")
else:
    print("NO")
