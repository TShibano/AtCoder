# ABC158B
N, A, B = map(int, input().split())
if A == 0:
    print(0)
    exit()
sho = N // (A + B)
amari = N % (A + B)
if amari >= A:
    amari = A
ans = sho * A + amari
print(ans)