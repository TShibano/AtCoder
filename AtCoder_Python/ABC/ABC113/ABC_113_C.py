# ABC113C
N, M = map(int, input().split())
NPM = [[0] * 3 for _ in range(M)]
for i in range(M):
    p, m = map(int, input().split())
    NPM[i][0] = i
    NPM[i][1] = p
    NPM[i][2] = m

NPM.sort(key = lambda x:(x[2]))

##print(NPM)
city_num = [0] * N
ans_list = [""] * M
for i in range(M):
    city_num[NPM[i][1]-1] += 1

    ans_list[NPM[i][0]] = "{:0>6}{:0>6}".format(NPM[i][1], city_num[NPM[i][1]-1])

for i in range(M):
    print(ans_list[i])