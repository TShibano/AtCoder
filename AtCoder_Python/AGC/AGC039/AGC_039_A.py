# AGC039A
def RanLengthEncoding(S):
    N = len(S)
    RLE = []
    now_char = S[0]
    now_cnt = 1
    for i in range(1, N):
        if now_char == S[i]:
            now_cnt += 1
        else:
            RLE.append([now_char, now_cnt])
            now_char = S[i]
            now_cnt = 1
    RLE.append([now_char, now_cnt])
    return RLE

S = input()
K = int(input())
rle = RanLengthEncoding(S)
if len(rle) == 1:
    ans = rle[0][1] * K // 2
    print(ans)
    exit()
cnt = 0
for i in range(1, len(rle)-1):
    cnt += rle[i][1] // 2

if rle[0][0] != rle[-1][0]:
    cnt += rle[0][1] // 2
    cnt += rle[-1][1] // 2
    ans = cnt * K
else:
    tmp = (rle[0][1] + rle[-1][1]) // 2
    ans = cnt * K
    ans += tmp * (K-1)
    ans += rle[0][1] // 2
    ans += rle[-1][1] // 2
print(ans)
