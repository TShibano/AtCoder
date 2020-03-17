# B
import math
H, W = map(int, input().split())
if H == 1 or W == 1:
    ans = 1
else:
    ans = math.ceil(H * W /  2)
print(ans)