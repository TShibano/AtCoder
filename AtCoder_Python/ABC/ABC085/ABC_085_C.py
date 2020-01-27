# ABC085C
N, Y = map(int, input().split())
flag = False
for a in range(N+1):
    for b in range(N-a+1):
        c = N - a - b
        if 10000 * a + 5000 * b + 1000 * c == Y and c >= 0:
            flag = True
            break
    if flag:
        break
if flag:
    print('{} {} {}'.format(a, b, c))
else:
    print('-1 -1 -1')
