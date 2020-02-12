# ABC140D
N, K = map(int, input().split())
S = input()
RLE = []
now_char = S[0]
cnt = 1

# ランレングス圧縮
for i in range(1, N):
    if S[i] == now_char:
        cnt += 1
    else:
        RLE.append([now_char, cnt])
        now_char = S[i]
        cnt = 1
RLE.append([now_char, cnt])

n = len(RLE)
if n//2 <= K:
    print(N-1)
    exit()
print(N - n + 2 * K)