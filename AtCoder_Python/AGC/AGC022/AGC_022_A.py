# AGC022A
S = input()
al=[chr(ord('a') + i) for i in range(26)]

if S == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
    exit()

if len(S) != 26:
    check =[[0] * 2 for _ in range(26)]
    for i in range(len(S)):
        for a in range(26):
            if S[i] == al[a]:
                check[a][0] = 1
                check[a][1] = i
    for i in range(26):
        if check[i][0] == 0:
            used_al = al[i]
            break
    print(S + used_al)
    exit()
ans = ""
lst = []
for i in range(24, -1, -1):
    if S[i] > S[i+1]:
        lst.append(S[i+1])
    else:
        lst.append(S[i+1])
        tmp = S[i]
        lst.append(S[i])
        ans += S[:i]
        lst.sort()
        for j in range(len(lst)):
            if tmp == lst[j]:
                ans += lst[j+1]
                break
        print(ans)
        exit()
