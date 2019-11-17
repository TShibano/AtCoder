# ABC145C
def fact(N):
    ans = 1
    for i in range(2, N+1):
        ans *= i
    return ans

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
distance_list = []
for i in range(N-1):
    for k in range(i+1, N):
        distance_list.append(((xy[i][0] - xy[k][0]) ** 2 + (xy[i][1] - xy[k][1]) ** 2) ** 0.5)
##print(distance_list)
tmp = sum(distance_list)
cnt = fact(N-1) * 2
##print(tmp, cnt, fact(N))
print(tmp * cnt / fact(N))