# D
N = int(input())
S = list(input())

ans = 0
for i in range(1000):
    if i <= 9:
        if S.count("0") >= 2:
            first = S.index("0")
            SS = S[first+1:]
            second = SS.index("0")
            SSS = SS[second+1:]
            tmp = str(i)
            if SSS.count(tmp) == 0:
                continue
            ans += 1
            ##print(i)
        else:
            continue
    elif i <= 99:
        if S.count("0") >= 1:
            first = S.index("0")
            SS = S[first+1:]
            tmp = str(i)
            if SS.count(tmp[0]) == 0:
                continue
            second = SS.index(tmp[0])
            SSS = SS[second+1:]
            if SSS.count(tmp[1]) == 0:
                continue
            ans += 1
            ##print(i)
        else:
    
            continue
    else:
        tmp = str(i)
        ##print(tmp)
        if S.count(tmp[0]) == 0:
            continue
        first = S.index(tmp[0])
        SS = S[first+1:]
        if SS.count(tmp[1]) == 0:
            continue
        second = SS.index(tmp[1])
        SSS = SS[second+1:]
        if SSS.count(tmp[2]) == 0:
            continue
        ##print(i)
        ans += 1

print(ans)
