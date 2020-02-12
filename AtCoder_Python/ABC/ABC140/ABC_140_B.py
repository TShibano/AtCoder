# ABC140B
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

prev = -2
ans = 0
for a in A:
    if a == prev+1:
        ans += C[prev-1]
    ans += B[a-1]
    prev = a
print(ans)