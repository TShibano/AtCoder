mod = 1000000007
N = int(input())
A = list(map(int, input().split()))

num_table = [0] * N
ans = 1
for i in range(N):
    if A[i] == 0:
        ans *= (3 - num_table[A[i]])
        num_table[A[i]] += 1
        continue
    ans *= (num_table[A[i] - 1] - num_table[A[i]])
    ans %= mod
    num_table[A[i]] += 1

print(ans)