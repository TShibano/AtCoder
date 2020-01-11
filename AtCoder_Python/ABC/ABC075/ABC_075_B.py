# ABC075B
H, W = map(int, input().split())
S = []
for i in range(H+2):
    if i == 0 or i == H+1:
        S.append('x' * (W+2))
    else:
        S.append('x' + input() + 'x')
        
for i in range(1, H+1):
    ans_tmp_str = ''
    for k in range(1, W+1):
        ans_tmp = 0   # count of bomb
        # print(S[i][k])
        if S[i][k] == '.':
            if S[i - 1][k - 1] == '#':
                ans_tmp += 1
            if S[i - 1][k] == '#':
                ans_tmp += 1
            if S[i - 1][k + 1] == '#':
                ans_tmp += 1
            if S[i][k - 1] == '#':
                ans_tmp += 1
            if S[i][k + 1] == '#':
                ans_tmp += 1
            if S[i + 1][k - 1] == '#':
                ans_tmp += 1
            if S[i + 1][k] == '#':
                ans_tmp += 1
            if S[i + 1][k + 1] == '#':
                ans_tmp += 1
            ans_tmp_str += str(ans_tmp)
           # print(ans_tmp_str)
        elif S[i][k] == '#':
            ans_tmp_str += '#'
    print(ans_tmp_str)
