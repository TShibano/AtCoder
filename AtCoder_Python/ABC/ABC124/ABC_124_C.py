# ABC124C
S = input()
N = len(S)
if 2 == N:
    S_0 = "01" * (N // 2)
    S_1 = "10" * (N // 2)
else:
    S_0 = "01" * (N // 2) + "0"
    S_1 = "10" * (N // 2) + "1"

cnt_0 = 0
cnt_1 = 0
for i in range(N):
    if S[i] != S_0[i]:
        cnt_0 += 1
    if S[i] != S_1[i]:
        cnt_1 += 1

print(min(cnt_0, cnt_1))
