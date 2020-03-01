# A
N = int(input())
s = [""] * N
t = [0] * N
for i in range(N):
    a, b = map(str, input().split())
    s[i] = a
    t[i] = int(b)
X = input()

sleep_index = s.index(X)
ans = 0
for i in range(sleep_index+1, N):
    ans += t[i]

print(ans)