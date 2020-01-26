# ABC079B

def luca_memo(n):
    memo = [0] * (n+1)
    
    def luca(n):
        if n == 0:
            return 2
        if n ==1:
            return 1
        if memo[n] != 0:
            return memo[n]
        memo[n] = luca(n-2) + luca(n-1)
        return memo[n]
    return luca(n)
N = int(input())
print(luca_memo(N))
