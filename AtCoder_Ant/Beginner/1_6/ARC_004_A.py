# ARC004A
def distance(A, B):     # A, B = [x, y]
    return ((A[0] - B[0])**2 + (A[1] - B[1]) ** 2) ** 0.5
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
distance_list = []
for i in range(N-1):
    for k in range(i+1, N):
        distance_list.append(distance(xy[i], xy[k]))
print(max(distance_list))