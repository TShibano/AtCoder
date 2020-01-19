# ABC152D
N = int(input())
len_N = len(str(N))
str_N = str(N)
N_a = int(str_N[0])
N_b = int(str_N[-1])
ans = 0
if len_N == 1:
    print(N)
    exit()
if len_N == 2:
    ans += 9
    for i in range(11, N+1):
        str_i = str(i)
        if str_i[1] == '0':
            continue
        i_tmp = int(str(i)[1] + str(i)[0])
        if i_tmp <= N:
            ans += 1
    tmp = N // 11
    ans += tmp * 2
    print(ans)
    exit()

for i in range(1, N+1):
    tmp = str(i)
    tmp_a = int(tmp[0])
    tmp_b = int(tmp[-1])
    if tmp_b == 0:
        continue
    if tmp_a == tmp_b:
        ans += 1
 
    if tmp_b > N_a:
        ans += int('1' * (len_N - 2))

    elif tmp_b == N_a and tmp_a <= N_b:
        ans += int('1' * (len_N - 2))
        naka = str_N[1:-1]
        if naka == "":
            continue
        ans += int(naka) + 1

    elif tmp_b == N_a and tmp_a > N_b:
        ans += int('1' * (len_N - 2))
        naka = str_N[1:-1]
        if naka == "":
            continue
        ans += int(naka)

    else:
        ans += int('1' * (len_N - 1))

print(ans)
