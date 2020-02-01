# ABC121C
N, M = map(int, input().split())

ab = [0] * N 
for i in range(N):
    ab[i] = list(map(int, input().split()))

ab = sorted(ab)
honsu = 0
money = 0
flag = False
for i in range(N):
    if flag:
        break
    count = ab[i][1]
    for k in range(count):
        if honsu == M:
            flag = True
            break
        else:
            money += ab[i][0]
            honsu += 1
print(money)
