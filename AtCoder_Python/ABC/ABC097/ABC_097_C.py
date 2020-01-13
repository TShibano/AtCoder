# ABC097C
S = input()
K = int(input())
N = len(S)

al = [chr(ord('a') + i) for i in range(26)]
tmp_al = []
if K==1:
    for s in al:
        if s in S:
            print(s)
            exit()

for s in al:
    if s in S:
        if len(tmp_al) == 3:
            break
        if N - S.rfind(s) >= K:
            tmp_al.append(s)
            break
        else:
            if N - S.find(s) >= K:
                tmp_al.append(s)
                break
            else:
                tmp_al.append(s)
                continue

count = [[] for _ in range(len(tmp_al))]
for i in range(len(tmp_al)):
    for k in range(N):
        if S[k] == tmp_al[i]:
            count[i].append(k)
ans_list = []
ans_list.append(tmp_al[0])
for i in count[0]:
    cnt = 1
    while (i + cnt <= N):
        if cnt == 7:
            break
        ans_list.append(S[i:i+cnt])
        cnt += 1

ans_list = list(set(ans_list))

if len(ans_list) < K:
    for i in count[1]:
        cnt = 1
        while (i + cnt <= N):
            if cnt == 7:
                break
            ans_list.append(S[i:i+cnt])
            cnt += 1
ans_list = list(set(ans_list))

if len(ans_list) < K:
    for i in count[2]:
        cnt = 1
        while i + cnt <= N:
            ans_list.append(S[i:i+cnt])
            cnt += 1
ans_list = list(set(ans_list))


ans_list.sort()
##print(ans_list)
print(ans_list[K-1])