# ABC044A
N = int(input())
K = int(input())
X = int(input())
Y = int(input())
if N>K:
    ans = K*X + (N-K)*Y
else:
    ans = N*X
print(ans)
