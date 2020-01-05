# ABC098B
N = int(input())
S = input()
ans_list = []
for i in range(1, N):
    tmp = 0
    A = list(set(S[0:i]))
    B = list(set(S[i:N]))
    for k in A:
        if k in B:
            tmp += 1   
    ans_list.append(tmp)
print(max(ans_list))
