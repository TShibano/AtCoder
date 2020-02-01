# ABC121D
A, B = map(int, input().split())
ans_list = []
ans = ""
b_cnt = len(bin(B)[2:])

a_list = [0] * b_cnt
b_list = [0] * b_cnt
diff = B - A + 1
for i in range(b_cnt):
    a_tmp = A % (2 ** (i + 1))
    b_tmp = B % (2 ** (i + 1))
    a_list[i] = a_tmp
    b_list[i] = b_tmp

# 下 2 桁より大きい桁はブロック(2 ** i)を考えてその中の 1 の個数を考える
for i in range(b_cnt):
    a = a_list[i]
    b = b_list[i]
    cnt = 0
    if i == 0:
        if a == b == 1:
            cnt += diff//2 + 1
        else:
            cnt += diff//2
    else:
        # A の1の個数をカウント
        if 2 ** i > a:
            cnt += 0
        else:
            cnt += 2 ** (i+1) - a
        # B の 1 の個数をカウント
        if 2 ** i > b:
            cnt += 0
        else:
            cnt += b - 2 ** i + 1
    if cnt % 2 == 0:
        ans_list.append("0")
    else:
        ans_list.append("1")

for i in range(len(ans_list) - 1, -1, -1):
    ans += ans_list[i]

print(int(ans, 2))


# 解説の仕方
# XOR の重要な性質
#       任意の偶数 n について n ^ (n+1) = 1
A, B = map(int, input().split())
a = A % 2
b = B % 2

diff = B - A + 1

if a == 0 and b == 0:
    diff -= 1
    ans = 1 ^ B if diff % 4 == 2 else B    
elif a == 0 and b == 1:
    ans = 1 if diff % 4 == 2 else 0
elif a == 1 and b == 0:
    diff -= 2
    ans = A ^ 1 ^ B if diff % 4 == 2 else A ^ B
else:
    diff -= 1
    ans = A ^ 1 if diff % 4 == 2 else A
print(ans)
