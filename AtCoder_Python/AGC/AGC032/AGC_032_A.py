# AGC032A-解説見た
# 逆を考えて右端からB[k] = k+1が一致したところを取り出していく
N = int(input())
B = list(map(int, input().split()))
ans_list = []
for i in range(N):
    for k in range(len(B)-1, -1, -1):
        if B[k] == k+1:
            ans_list.append(B[k])
            del B[k]
            break
        if k == 0:
            print(-1)
            exit()
for k in range(len(ans_list)):
    print(ans_list[- 1 - k])