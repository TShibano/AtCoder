# ABC151C
N, M = map(int, input().split())
P = [0] * M
S = [""] * M

check_AC = [False] * N
for i in range(M):
    p, s = map(str, input().split())
    p = int(p)
    if s == "AC":
        check_AC[p-1] = True
    P[i] = p
    S[i] = s

ans_AC = 0
ans_WA = 0
for i in range(M):
    if check_AC[P[i]-1]:
        if S[i] == "AC":
            ans_AC += 1
            check_AC[P[i] - 1] = False
        else:
            ans_WA += 1
    else:
        continue
print(ans_AC, ans_WA)
