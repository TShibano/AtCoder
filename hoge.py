# ABC122-C
N, Q = map(int, input().split())
S = input()
lr = [list(map(int, input().split())) for _ in range(Q)]
ind = []
for i in range(N-1):
    if S[i] == "A" and S[i+1] == "C":
        ind.append(i+1)
cnt_list = [0] * N
tmp = 0
for i in range(N):
    if i in ind:
        tmp += 1
    cnt_list[i] = tmp
print(cnt_list)

for i in range(Q):
    l = lr[i][0] - 1
    r = lr[i][1] - 1
    print(cnt_list[r] - cnt_list[l])
