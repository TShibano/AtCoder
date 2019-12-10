# ABC147C
N = int(input())
enter = []
A = [0] * N
for a in range(N):
    ai = int(input())
    tmp_enter = [list(map(int, input().split())) for _ in range(ai)]
    A[a] = ai
    enter.append(tmp_enter)

ans_list = [0]
for i in range(2 ** N):
    # iは誰が正直者かを表す
    honest = []
    unkind = []
    flag = True
    for j in range(N):
        if (i >> j) & 1:
            honest.append(j)
        else:
            unkind.append(j)
    ##print(i, honest, unkind)
    for h in honest:
        for k in range(A[h]):
            if enter[h][k][1] == 1:
                if (enter[h][k][0]-1) in unkind:
                    flag = False
                    break
            if enter[h][k][1] == 0:
                if (enter[h][k][0]-1) in honest:
                    flag = False
                    break
    if flag:
        ans_list.append(len(honest))
print(max(ans_list))