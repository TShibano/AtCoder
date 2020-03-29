# C

S = input()
N = len(S)
# 回分判定
ss = ""
for s in S:
    if s == 'x':
        pass
    else:
        ss += s
if ss != ss[::-1]:
    print(-1)
    exit()
if ss == "":
    print(0)
    exit()
# 真ん中を決める
# x の位置と個数を求める
n = len(ss)
if n % 2 == 0:
    cnt = 0
    for i in range(n//2+1):
        for j in range(cnt, N):
            if S[j] == "x":
                continue
            else:
                cnt = j+1
                break
        if i == n//2-1:
            left_center = cnt-1
    right_center = cnt-1
    # 真ん中の分を先に計算する
    ans = (abs(right_center - left_center) % 2)
    # centerから両側に展開していく
    count = 0
    x_left = []
    x_right = []
    for i in range(left_center):
        if S[left_center-1 - i] == 'x':
            count += 1
        else:
            x_left.append(count)
            count = 0
    x_left.append(count)
    count = 0
    for i in range(right_center+1, N, 1):
        if S[i] == 'x':
            count += 1
        else:
            x_right.append(count)
            count = 0
    x_right.append(count)
    ans = 0
    for i in range(len(x_left)):
        ans += abs(x_left[i] - x_right[i])
    print(ans)
else:
    cnt = 0
    for i in range(n//2+1):
        for j in range(cnt, N):
            if S[j] == "x":
                continue
            else:       # S[j] != "x" なら ss[i] と S[j] は一致する
                cnt = j + 1
                break
    center = cnt-1
    # print(center)
    # center から両側に展開していき，center からの位置と x の個数を求める
    distans = 0     # x 以外の文字が出るたびに更新する
    count = 0
    x_left = []
    x_right = []
    # 位置を記憶する必要はない．
    for i in range(center):
        if S[center-1 - i] == "x":
            count += 1
        else:
            x_left.append([distans, count])
            distans += 1
            count = 0
    x_left.append([distans, count])
    distans = 0
    count = 0
    for i in range(center+1, N):
        if S[i] == "x":
            count += 1
        else:
            x_right.append([distans, count])
            distans += 1
            count = 0
    x_right.append([distans, count])
    # print(x_left)
    # print(x_right)
    ans = 0
    for i in range(len(x_left)):
        ans += abs(x_left[i][1] - x_right[i][1])
    print(ans)

# 解説の解き方
S = input()
N = len(S)
r = 0       # 末尾の位置
l = 0       # 先頭の位置
ans = 0
while l+r < N:                  # 両者が同じところにきたら終わり．
    if S[l] == S[N-1 - r]:      # 同じなら先頭と末尾を進める
        l += 1
        r += 1
    else:
        if S[l] == 'x':     # 先頭が x なら先頭を進める
            l += 1
            ans += 1
        elif S[N-1 - r] == 'x':     # 末尾が x なら末尾を進める
            r += 1
            ans += 1
        else:
            print(-1)
            exit()

print(ans)