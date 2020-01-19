# ABC110C
import collections
S = input()
T = input()

s = collections.Counter(S)
t = collections.Counter(T)

ss = s.most_common()
tt = t.most_common()

if len(ss) != len(tt):
    print("No")
    exit()

for i in range(len(ss)):
    if ss[i][1] != tt[i][1]:
        print("No")
        exit()

print("Yes")
