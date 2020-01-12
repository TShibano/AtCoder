# ABC084C
N = int(input())
C = [0] * (N-1)
S = [0] * (N-1)
F = [0] * (N-1)
for i in range(N-1):
    c, s, f = map(int, input().split())
    C[i] = c
    S[i] = s
    F[i] = f

ans_list = [0] * N
for i in range(N-1):
    time = 0
    time = C[i] + S[i]
    for k in range(i+1, N-1):
        if time < S[k]:
            time = S[k] + C[k]
        else:
            time += (S[k] - time) % F[k]
            time += C[k]
    ans_list[i] = time

for i in range(N):
    print(ans_list[i])