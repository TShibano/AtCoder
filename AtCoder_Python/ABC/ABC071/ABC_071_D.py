# ABC071D
mod = 10 ** 9 + 7
N = int(input())
S1 = input()
S2 = input()

domino = []     # 0 : 横, 1 : 縦
flag = False
for i in range(N):
    if S1[i] == S2[i]:
        domino.append(1)
        flag = False
    else:
        if flag:
            flag = False
        else:
            domino.append(0)
            flag = True

if domino[0] == 0:
    ans = 6
else:
    ans = 3

for i in range(1, len(domino)):
    if domino[i] == 0:
        if domino[i-1] == 0:
            ans *= 3
        else:
            ans *= 2
    else:
        if domino[i-1] == 0:
            ans *= 1
        else:
            ans *= 2
print(ans%mod)