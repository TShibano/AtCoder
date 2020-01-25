# ABC071C
N = int(input())
A = sorted(list(map(int, input().split())), reverse = True)

for i in range(N-1):
    if A[i] == A[i+1]:
        A[i+1] = 0
    elif A[i] != A[i+1]:
        A[i] = 0
A.sort(reverse = True)
print(A[0] * A[1])
