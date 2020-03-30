# B
S = input()
N = len(S)
cnt_list = [0, 0, 0]
for s in S:
    if s == 'a':
        cnt_list[0] += 1
    elif s == 'b':
        cnt_list[1] += 1
    else:
        cnt_list[2] += 1
tmp = N % 3 
if tmp == 0:
    if N // 3 == max(cnt_list) and N // 3 == min(cnt_list):
        ans = "YES"
    else:
        ans = "NO"
elif tmp == 1:
    cnt_list.sort()
    if cnt_list[0] == cnt_list[1] and cnt_list[2] == N//3+1:
        ans = "YES"
    else:
        ans = "NO"
else:
    cnt_list.sort()
    if cnt_list[0] == N//3 and cnt_list[1] == cnt_list[2]:
        ans = "YES"
    else:
        ans = "NO"
print(ans)