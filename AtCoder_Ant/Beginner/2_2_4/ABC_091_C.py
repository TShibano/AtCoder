# ABC091C
# 解説をみた
# 青い点のうち，x座標が最小のものを考えて，ペアにできる赤い点を考える
# そのうち，赤い点のy座標が最大のものをとる
N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]
cd = [list(map(int, input().split())) for _ in range(N)]
cd.sort()
ans = 0

for i in range(N):
    blue_x , blue_y = cd[i][0], cd[i][1]
    red_list_x = []
    red_list_y = []
    red_list_index = []
    for k in range(len(ab)):
        red_x, red_y = ab[k][0], ab[k][1]
        if blue_x > red_x and blue_y > red_y:
            red_list_x.append(red_x)
            red_list_y.append(red_y)
            red_list_index.append(k)
    if red_list_index:
        loc = red_list_index[red_list_y.index(max(red_list_y))]
        ans += 1
        del ab[loc]
        

print(ans)