# C
al = [chr(ord('a') + i) for i in range(26)]

H, W = map(int, input().split())
A = [input() for _ in range(H)]

cnt = [0] * 26
for h in range(H):
    for w in range(W):
        cnt[al.index(A[h][w])] += 1
cnt = [i for i in cnt if i != 0]
cnt.sort(reverse=True)

if H % 2 == 1 and W % 2 == 1:
    count = (H//2) * (W//2)
    while count > 0:
        count -= 1
        cnt[0] -= 4
        cnt.sort(reverse=True)
    cnt = [i for i in cnt if i != 0]
    count = (H//2) + (W//2)
    while count > 0:
        count -= 1
        cnt[0] -= 2
        cnt.sort(reverse=True)
    cnt = [i for i in cnt if i != 0]
    if sum(cnt) == 1 and len(cnt) == 1:
        ans = "Yes"
    else:
        ans = "No"
elif H % 2 == 0 and W % 2 == 0:
    count = (H//2) * (W//2)
    while count > 0:
        count -= 1
        cnt[0] -= 4
        cnt.sort(reverse=True)
    cnt = list(set(cnt))
    if cnt[0] == 0 and len(cnt) == 1:
        ans = "Yes"
    else:
        ans = "No"
else:
    count = (H//2) * (W//2)
    while count > 0:
        count -= 1
        cnt[0] -= 4
        cnt.sort(reverse=True)
    cnt = [i for i in cnt if i != 0]
    cnt.sort(reverse=True)
    count = (H%2) * (W//2) + (H//2) * (W%2)
    while count > 0:
        count -= 1
        cnt[0] -= 2
        cnt.sort(reverse=True)
    cnt =list(set(cnt))
    if cnt[0] == 0 and len(cnt) == 1:
        ans = "Yes"
    else:
        ans = "No"
print(ans)