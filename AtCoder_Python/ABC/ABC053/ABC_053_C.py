# ABC053C
x = int(input())
sho = x // 11
amari = x % 11
if 0 == amari:
    print(sho * 2)
elif 0 < amari <= 6:
    print(sho * 2 + 1)
else:
    print(sho * 2 + 2)
