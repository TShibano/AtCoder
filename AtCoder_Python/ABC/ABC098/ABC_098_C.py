# ABC098C
N = int(input())
S = input()

all_W_E = [0, 0]
for s in S:
    if s == "W":
        all_W_E[0] += 1
    else:
        all_W_E[1] += 1

now_W = 0
now_E = 0
ans_list = [0] * N

for i in range(N):
    if S[i] == "W":
        ans_list[i] = (now_W + all_W_E[1] - now_E)
        now_W += 1
    else:
        ans_list[i] = (now_W + all_W_E[1] - now_E - 1)
        now_E += 1

##print(ans_list)
print(min(ans_list))