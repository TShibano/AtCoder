# ABC157C
N, M = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(M)]
sc = list(map(list, set(map(tuple, sc))))
M = len(sc)
if N == 1:
    if M == 1:
        print(sc[0][1])
        exit()
    if M == 0:
        print(0)
        exit()

tmp = [-1] * N
for i in range(M):
    if sc[i][0] == 1 and sc[i][1] == 0:
        print(-1)
        exit()

    if tmp[sc[i][0]-1] == -1:
        tmp[sc[i][0]-1] = sc[i][1]
    else:
        print(-1)
        exit()

if tmp[0] == -1:
    tmp[0] = 1
ans = ""
for i in range(N):
    if tmp[i] == -1:
        ans += "0"
    else:
        ans += str(tmp[i])
print(int(ans))