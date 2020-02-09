# ABC133C
L, R = map(int, input().split())
l = L % 2019
r = R % 2019
ans = []
if R - L >= 2019:
    print(0)
else:
    if l >= r:
        print(0)
    else:
        for i in range(l, r):
            for k in range(l+1, r+1):
                ans.append(i * k % 2019)                
    print(min(ans))                
