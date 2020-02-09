# ABC130D
N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

# 尺取り法
right = 0
tmp = 0
for i in range(N):
    for k in range(right, N, 1):
        tmp += A[k]
        if tmp >= K:
            right = k
            ans += N - right
            tmp -= A[i]
            tmp -= A[right]
            break
        if k == N-1:
            tmp -= A[k]
            tmp -= A[i]
            right = k
            break 

print(ans)


# while文を書いた法
N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

# 尺取り法
right = 0   # 使い回す
wa = 0      # 使い回す
for left in range(N):
    while right < N and wa + A[right] < K:
        wa += A[right]
        right += 1
    ans += (N - right)
    if right == left:
        right += 1
    else:
        wa -= A[left]

print(ans)