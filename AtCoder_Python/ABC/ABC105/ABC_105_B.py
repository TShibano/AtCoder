# ABC105B
N = int(input())
ans = "No"
for i in range(N//4 + 1):
    for k in range(N//7 + 1):
        if 4*i + 7*k == N:
            ans = "Yes"

print(ans)