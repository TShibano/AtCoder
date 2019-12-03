# ABC005C
# 方針：ソートされているから1番目の客から渡せるたこ焼きがあるかを考えていく．
# あったらそのたこ焼きを除く．渡せるものがないならダメ
# もっと上手な仕方がありそう
T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

if N < M:
    print("no")
    exit()

for b in B:
    for a in range(len(A)):
        if A[a] <= b <= A[a] + T:
            del A[a]
            break
        if a == len(A) - 1:
            print("no")
            exit()

print("yes")