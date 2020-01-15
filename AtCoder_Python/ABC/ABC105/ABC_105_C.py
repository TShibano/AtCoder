# ABC105C
N = int(input())
if N == 0:
    print(0)
    exit()
ans = ""
while N != 1:
    if N % 2 == 0:
        N //= (-2)
        ans = "0" + ans
    else:
        if N > 0:
            N //= (-2)
            N += 1
            ans = "1" + ans
        else:
            N //= (-2)
            N += 1
            ans = "1" + ans
ans = "1" + ans    
print(ans)