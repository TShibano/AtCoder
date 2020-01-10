# ABC050B
N = int(input())
T = list(map(int, input().split()))
M = int(input())
px = []
for i in range(M):
    px.append(list(map(int, input().split())))
for i in range(M):
    ans = 0
    ans += sum(T) - T[px[i][0]-1] + px[i][1]
    print(ans)
