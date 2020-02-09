# ABC133D
N = int(input())
A = list(map(int, input().split()))

ans_list = [0] * N

wa = sum(A)
A = list(map(lambda x:x * 2, A))
tmp = 0
for i in range(0, N-1, 2):
    tmp += A[i]
ans_list[-1] = wa - tmp
for i in range(N-2, -1, -1):
    ans_list[i] = A[i] - ans_list[i+1]

print(" ".join(map(str, ans_list)))
