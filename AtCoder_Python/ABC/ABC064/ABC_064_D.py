# ABC064D
N = int(input())
S = input()

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


n = len(RLE)
ans = ""
left_cnt = 0
right_cnt = 0

for i in range(n):
    now_char = RLE[i][0]
    now_cnt = RLE[i][1]
    if now_char == "(":
        left_cnt += now_cnt
    else:
        right_cnt += now_cnt
        if right_cnt > left_cnt:
            ans += "(" * (right_cnt - left_cnt)
            right_cnt = 0
            left_cnt = 0
        else:
            left_cnt -= right_cnt
            right_cnt = 0

ans += S
if left_cnt > 0:
    ans += ")" * left_cnt

print(ans)

