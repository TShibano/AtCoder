# ABC142C
N = int(input())
A = list(map(int, input().split()))
ans = [0] * N
cnt = 1
for a in A:
    ans[a-1] = str(cnt)
    cnt += 1
print(" ".join(ans))