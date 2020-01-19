# ABC112C
N = int(input())
X = [0] * N
Y = [0] * N
H = [0] * N

for i in range(N):
    x, y, h = map(int, input().split())
    X[i] = x
    Y[i] = y
    H[i] = h

for cx in range(101):
    for cy in range(101):
        H_list = []
        check_list = []
        for i in range(N):
            if H[i] == 0:
                check_list.append(i)
                continue
            H_list.append(H[i] + abs(X[i] - cx) + abs(Y[i] - cy))
        if len(set(H_list)) == 1:
            h = H_list[0]
            flag = True
            for check in check_list:
                if H[check] == max(h - abs(X[check] - cx) - abs(Y[check] - cy), 0):
                    pass
                else:
                    flag = False
                    break
            if flag:
                print(cx, cy, h)
                exit()
