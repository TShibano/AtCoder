# ABC152B
a, b = map(int, input().split())

if a > b:
    ans = str(b) * a
else:
    ans = str(a) * b

print(ans)
