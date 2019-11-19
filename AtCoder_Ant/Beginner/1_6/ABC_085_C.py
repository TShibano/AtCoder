N, Y = map(int, input().split())
y = Y // 1000
ans = [-1, -1, -1]
# 10*a + 5*b + c == y and N == a + b + c
for a in range(N+1):
    for b in range(N+1):
        c1 = y - 10 * a - 5 * b
        c2 = N - b - a
        if c1 == c2 and c2 >= 0:
            ans = [a, b, c1]
            break
print(" ".join(map(str, ans)))