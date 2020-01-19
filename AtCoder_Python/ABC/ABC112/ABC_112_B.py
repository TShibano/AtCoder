# ABC112B
N, T = map(int, input().split())
ct = []
for i in range(N):
    ct.append(list(map(int, input().split())))
ans_list = []
for i in range(N):
    if ct[i][1] <= T:
        ans_list.append(ct[i][0])

if len(ans_list) == 0:
    print("TLE")
else:
    print(min(ans_list))
