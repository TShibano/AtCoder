# ABC149D
def score(c):
    if c == "r":
        return R
    if c == "s":
        return S
    if c == "p":
        return P
N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

new_T = [""] * N
for i in range(N):
    if T[i] == "r":
        new_T[i] = "p"
    if T[i] == "s":
        new_T[i] = "r"
    if T[i] == "p":
        new_T[i] = "s"

ans = 0
for i in range(N):
    if i < K:
       ans += score(new_T[i]) 
    else:
        if new_T[i] == new_T[i-K]:
            new_T[i] = "x"
        else:
            ans += score(new_T[i])

print(ans)