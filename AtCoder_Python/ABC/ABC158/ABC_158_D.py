# ABC158D
S = input()
Q = int(input())
Query = [input() for _ in range(Q)]
flag = True
forward = ""
backward = ""
for i in range(Q):
    if Query[i][0] == "1":
        if flag:
            flag = False
        else:
            flag = True
    else:
        if Query[i][2] == '1':
            if flag:
                forward = Query[i][4] + forward
            else:
                backward = backward + Query[i][4]
        else:
            if flag:
                backward = backward + Query[i][4]
            else:
                forward = Query[i][4] + forward

if flag:
    ans = forward + S + backward
else:
    forward = forward[::-1]
    backward = backward[::-1]
    S = S[::-1]
    ans = backward + S + forward
print(ans)