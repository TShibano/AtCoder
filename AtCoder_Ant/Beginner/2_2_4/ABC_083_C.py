# ABC083C
# 方針：Xを2倍していく時最大の数となる
X, Y = map(int, input().split())
ans = 0
while X <= Y:
    X *= 2
    ans += 1
print(ans)

'''
# 方針：X * (2 ** ans) <= Yを満たすansを求める
# -> 2 ** ans <= Y // X

X, Y = map(int, input().split())
k = Y // X
ans = 1
while 2 ** ans <= k:
    ans += 1
print(ans)
'''