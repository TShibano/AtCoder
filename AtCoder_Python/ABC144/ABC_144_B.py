# ABC144B
N = int(input())
ans = "No"
for a in range(1, 10):
    b = N // a
    if 0 < b and b < 10 and N == a * b:
        ans = "Yes"
        break
print(ans)