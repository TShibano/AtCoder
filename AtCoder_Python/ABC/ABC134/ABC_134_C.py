# ABC134C
N = int(input())
A = [int(input()) for i in range(N)]
max_A = max(A)
B = set(A)
if len(B) == 1 or A.count(max_A) >= 2:
    for i in range(N):
        print(max_A)
else:
    C = list(A)
    for i in range(N):
        if A[i] == max_A:
            C.remove(max_A)
            print(max(C))
        else:
            print(max_A)
