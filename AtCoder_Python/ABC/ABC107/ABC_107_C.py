# ABC107C
N, K = map(int, input().split())
X = list(map(int, input().split()))

distans_list = [100000000000] * N
for i in range(N - K + 1):
    if X[i] < 0:
        if X[i+K-1] < 0:
            distans_list[i] = abs(X[i])
        else:
            if abs(X[i]) < abs(X[i+K-1]):
                distans_list[i] = 2 * abs(X[i]) + X[i+K-1]
            else:
                distans_list[i] = abs(X[i]) + 2 * X[i+K-1]
    else:
        distans_list[i] = X[i+K-1]
##print(distans_list)
print(min(distans_list))