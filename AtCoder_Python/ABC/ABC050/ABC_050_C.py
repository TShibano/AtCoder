# ABC050C
import collections
mod = 10 ** 9 + 7
N = int(input())
A = list(map(int, input().split()))
a = collections.Counter(A)
a = a.most_common()[::-1]

if N % 2 == 0:
    for i in range(len(a)):
        if a[i][0] % 2 == 1 and a[i][1] == 2:
            pass
        else:
            print(0)
            exit()
    ans = (2 ** (N // 2)) % mod

else:
    for i in range(len(a)):
        if a[i][0] == 0:
            if a[i][1] == 1:
                pass
            else:
                print(0)
                exit()
        else:
            if a[i][0] % 2 == 0 and a[i][1] == 2:
                pass
            else:
                print(0)
                exit()
    ans = (2 ** (N // 2)) % mod 
print(ans)