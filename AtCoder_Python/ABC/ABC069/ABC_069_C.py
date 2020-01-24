# ABC069C
N = int(input())
a = list(map(int, input().split()))

cnt4 = 0
cnt1 = 0
for i in range(N):
    if a[i] % 4 == 0:
        cnt4 += 1
    if a[i] % 2 != 0:
        cnt1 += 1

if cnt4 >= cnt1:
    print("Yes")
else:
    if N == cnt4 + cnt1 and cnt4 + 1 == cnt1:
        print("Yes")
    else:
        print("No")
