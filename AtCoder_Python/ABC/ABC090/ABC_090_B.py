# ABC090B
A, B = map(int, input().split())
ans = 0
for i in range(A, B+1):
    i = str(i)
    if i[0] == i[4] and i[1] == i[3]:
        ans += 1
print(ans) 
