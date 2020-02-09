# ABC130C
W, H, x, y = map(int, input().split())
s = W*H/2

if W % 2 == 0 and H % 2 == 0 and W // 2 == x and H // 2 == y:
    print(s, 1)
else:
    print(s, 0)
