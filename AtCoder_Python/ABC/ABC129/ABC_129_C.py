# ABC129C
import sys
sys.setrecursionlimit(10 ** 5 + 10)
mod = 10 ** 9 + 7

# フィボナッチ数列
fib_memo = {}
def fib(N):
    if N < 2: return 1
    if N not in fib_memo:
        fib_memo[N] = fib(N-1) + fib(N-2)
    return fib_memo[N]

N, M = map(int, input().split())
A = [int(input()) for _ in range(M)]

tmp_list = [0] * (M+1)
now_kaidan = 0
for i in range(M):
    tmp_list[i] = (A[i] - 1) - now_kaidan
    now_kaidan = A[i] + 1
tmp_list[-1] = N-now_kaidan
ans = 1

for v in tmp_list:
    if v == -1:     # 壊れた階段が連続している時は0移動方法がない
        print(0)
        exit()
    ans *= fib(v)
    ans %= mod

print(ans%mod)


# DP
mod = 10 ** 9 + 7
N, M = map(int, input().split())
A = [int(input()) for _ in range(M)]

if N == 1:
    print(1)
    exit()
if N == 2:
    if M == 0:
        print(2)
    if M == 1:
        print(1)
    exit()

safe = [True] * (N+1)
for i in range(M):
    safe[A[i]] = False 

dp = [0] * (N+1)
dp[0] = 0
dp[1] = 1
dp[2] = 2

if 1 in A:
    dp[1] = 0
    dp[2] = 1
if 2 in A:
    dp[2] = 0

for i in range(3, N+1):
    if safe[i]:
        dp[i] = dp[i-1] + dp[i-2]

##print(dp)
print((dp[N]+mod)%mod)