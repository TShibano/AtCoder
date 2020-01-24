# ABC069D
from collections import deque
H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

ans_list = [[0] * W for _ in range(H)]
ans = 0
cnt = 0
for h in range(H):
    if h % 2 == 0:
        for w in range(W):
            if cnt == A[ans]:
                cnt = 0
                ans += 1
            ans_list[h][w] = ans + 1
            cnt += 1
    else:
        for w in range(W-1, -1, -1):
            if cnt == A[ans]:
                cnt = 0
                ans += 1
            ans_list[h][w] = ans + 1
            cnt += 1

for a in ans_list:
    print(*a)