# ABC151B
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

sum_A = sum(A)

score = M * N - sum_A
if score < 0:
    print(0)
elif 0 <= score and score <= K:
    print(score)
else:
    print(-1)
