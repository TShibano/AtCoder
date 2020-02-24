# ABC155C
from collections import Counter
N = int(input())
S = [input() for _ in range(N)]

c = Counter(S)
cnt = 1
c = c.most_common()
for i in range(len(c)-1):
    if c[i][1] == c[i+1][1]:
        cnt += 1
    else:
        break
ans_list = [""] * cnt
for i in range(cnt):
    ans_list[i] = c[i][0]
ans_list.sort()
for i in range(cnt):
    print(ans_list[i])
