# ABC109B
N = int(input())
W = [0] * N
for i in range(N):
    W[i] = input()

flag = True
if N != len(set(W)):
    flag = False
if flag:
    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            flag  = False
            break
if flag:
    print("Yes")
else:
    print("No")
