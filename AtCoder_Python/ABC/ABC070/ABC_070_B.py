# ABC070B
a, b, c, d = map(int, input().split())
ans = 0
cd = []
for i in range(c, d):
    cd.append(i)
for i in range(a, b):
    if i in cd:
        ans += 1
print(ans)        
