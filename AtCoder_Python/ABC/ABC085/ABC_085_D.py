# ABC085D
import math
import copy
N, H = map(int, input().split())
a_max = [list(map(int, input().split())) for _ in range(N)]
b_max = copy.deepcopy(a_max)
b_max.sort(key=lambda x:-x[1])
a_max.sort(key=lambda x:-x[0])
damage = 0
cnt_damage = 0
for i in range(N):
    if damage >= H:
        print(cnt_damage)
        exit()
        
    if b_max[i][1] >= a_max[0][0]:
        damage += b_max[i][1]
        cnt_damage += 1
    else:
        break

cnt_damage += math.ceil((H-damage)/a_max[0][0])

print(cnt_damage)