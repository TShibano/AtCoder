# B
N = int(input())
XL = [list(map(int, input().split())) for _ in range(N)]
RL = [[0, 0] for _ in range(N)]
for i in range(N):
    left = XL[i][0] - XL[i][1]
    right = XL[i][0] + XL[i][1]
    RL[i][0] = left
    RL[i][1] = right

RL.sort(key=lambda x: x[1])
now_right = RL[0][1]
cnt = 0
for i in range(1, N):
    if now_right <= RL[i][0]:
        now_right = RL[i][1]
    else:
        cnt += 1
print(N - cnt)
