# ABC114C
N = int(input())
def dfs(num, use):
    if num > N:
        return 0
    cnt = 1 if use == 0b111 else 0
    cnt += dfs(num*10 + 3, use | 0b001)
    cnt += dfs(num*10 + 5, use | 0b010)
    cnt += dfs(num*10 + 7, use | 0b100)
    return cnt
ans = dfs(0, 0)
print(ans)
