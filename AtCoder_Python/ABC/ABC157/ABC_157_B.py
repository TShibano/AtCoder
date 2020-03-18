# ABC157B
A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
B = [int(input()) for _ in range(N)]

bingo = [[0] * 3 for _ in range(3)]

for i in range(N):
    for h in range(3):
        for w in range(3):
            if A[h][w] == B[i]:
                bingo[h][w] = 1

# H側
ans = "No"
for h in range(3):
    cnt = 0
    for w in range(3):
        if bingo[h][w]:
            cnt += 1
    if cnt == 3:
        ans = "Yes"

for w in range(3):
    cnt = 0
    for h in range(3):
        if bingo[h][w]:
            cnt += 1
    if cnt == 3:
        ans = "Yes"

cnt = 0
for a in range(3):
    if bingo[a][a]:
        cnt += 1
    if cnt == 3:
        ans = "Yes"
cnt = 0
for a, b in zip([0, 1, 2], [2, 1, 0]):
    if bingo[a][b]:
        cnt += 1
    if cnt == 3:
        ans = "Yes"
print(ans)
