# ABC084B
A, B = map(int, input().split())
S = input()
ans = 'No'
flag = True
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
if S[A] == '-':
    aa = S[0:A]
    bb = S[A+1:A+B+1]
    for i in range(len(aa)):
        if aa[i] not in num:
            flag  = False
    for k in range(len(bb)):
        if bb[k] not in num:
            flag = False
    if flag:
        ans = 'Yes'
print(ans)
