# B
path = [list(map(int, input().split())) for _ in range(3)]
cnt = [0, 0, 0, 0]
for i in range(3):
    cnt[path[i][0] - 1] += 1
    cnt[path[i][1] - 1] += 1
if 3 in cnt:
    print("NO")
else:
    print("YES")