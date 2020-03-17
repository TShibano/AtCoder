# D
N = int(input())

al = [chr(ord('a') + i) for i in range(26)]

ans = ['a']
for i in range(N-1):
    tmp = []
    for s in ans:
        stop = ord(max(s)) + 1
        for i in range(ord('a'), stop+1):
            tmp.append(s + chr(i))
    ans = tmp
for s in ans:
    print(s)


# ------------------------------------------

N = int(input())

alphabets = [chr(ord('a') + x) for x in range(26)]

def dfs(S, i):
    if len(S) == N:
        yield ''.join(S)
        return
    for j in range(i):
        for w in dfs(S + [alphabets[j]], i):
            yield w
    for w in dfs(S + [alphabets[i]], i + 1):
        yield w

for w in dfs([],0):
    print(w)

