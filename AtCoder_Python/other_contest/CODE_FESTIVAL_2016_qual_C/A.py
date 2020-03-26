# A
S = input()
ans = "No"
flag = False
for i in range(len(S)):
    if S[i] == 'C':
        flag = True
    if flag == True and S[i] == 'F':
        ans = "Yes"
print(ans)