# ABC071B
S = input()
ss = set()
for i in range(len(S)):
    ss.add(S[i])

alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                       'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ans = ''
for k in range(len(alpha_list)):
    if alpha_list[k] not in ss:
        ans = alpha_list[k]
        break
if len(ss) == 26:
    print('None')
else:
    print(ans)


S = input()
S = set(list(S))
alp = [chr(ord('a') + i) for i in range(26)]
for al in alp:
    if al in S:
        pass
    else:
        print(al)
        exit()
print("None")