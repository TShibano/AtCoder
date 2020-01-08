# ABC128B
N = int(input())
S = []
for i in range(N):
    s = list(input().split())
    s.append(i+1)
    S.append(s)
    
for i in range(N):
    S[i][1] = int(S[i][1])

S.sort(key=lambda x:(x[0], -x[1]))

for i in range(N):
    print(S[i][2])
    