# ABC146B
N = int(input())
S = input()
al1 = [chr(ord('A') + i) for i in range(26)]
al2 = [chr(ord('A') + i) for i in range(26)]
al = al1 + al2
ans = ""
for i in range(len(S)):
    ans += al[al.index(S[i]) + N]
print(ans)
