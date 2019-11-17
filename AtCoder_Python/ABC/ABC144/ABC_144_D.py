# ABC144D
import math
a, b, x = map(int, input().split())
h = x / (a ** 2)
if h > b / 2:
    l = (2 * b) - (2 * x / a / a)
    ans = math.degrees(math.atan(l / a))
elif 2 * x == a * a * b:
    ans = math.degrees(math.atan(b / a))
else:
    l = 2 * x / a / b
    ans = math.degrees(math.atan(b / l))
print("{:.10f}".format(ans))