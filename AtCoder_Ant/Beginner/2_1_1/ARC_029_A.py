# ARC029A
N = int(input())
t = [int(input()) for _ in range(N)]
t.sort()
if N == 1 or N == 2:
    print(max(t))
    exit()
if N == 3:
    print(max(t[0] + t[1] , t[2]))
    exit()

if N == 4:
    ans_list = []
    ans_list.append(max(t[0]+t[3], t[1]+t[2]))
    ans_list.append(max(t[0]+t[1]+t[2], t[3]))
    print(min(ans_list))
    exit()