# ABC108B
a, b, c, d = map(int, input().split())
# (x1, y1)を原点に移動させる
c -= a
d -= b
if c > 0 and d >= 0:     # 第一象限
    e = c - d
    f = c + d
    g = -abs(d)
    h = abs(c)
elif c <= 0 and d > 0:       # 第二象限
    e = c - abs(d)
    f = d - abs(c)
    g = -abs(d)
    h = -abs(c)
elif c < 0 and d <= 0:       # 第三象限
    e = c + abs(d)
    f = d - abs(c)
    g = abs(d)
    h = -abs(c)
else:       # 第四象限
    e = c + abs(d)
    f = d + abs(c)
    g = abs(d)
    h = abs(c)

print("{} {} {} {}".format(e+a , f+b , g+a ,h+b))
