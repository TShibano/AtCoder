# KUPC2015A
# 方針：手前からtokyo or kyotoを見つける

T = int(input())
S = [input() for _ in range(T)]

for i in range(T):
    tmp = S[i]
    ans = 0
    while "tokyo" in tmp or "kyoto" in tmp:
        a = tmp.find("tokyo")
        b = tmp.find("kyoto")
        if a == -1 and b == -1:     # tmpに"tokyo", "kyoto"がない
            print(ans)
            break
        else:
            if a == -1:     # "kyoto"のみ
                ans += 1
                tmp = tmp.replace("kyoto", "#", 1)
            elif b == -1:   # "tokyo"のみ
                ans += 1
                tmp = tmp.replace("tokyo", "#", 1)
            elif a < b:     # "tokyo"が先にある
                ans += 1
                tmp = tmp.replace("tokyo", "#", 1)
            elif b < a:     # "kyoto"が先にある
                ans += 1
                tmp = tmp.replace("kyoto", "#", 1)
    print(ans)