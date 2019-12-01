# ABC103D
# 貪欲法：区間スケジューリング問題に帰着
# ソートして喧嘩している遠い島(b[i])の最も近いところから貪欲に選んでいく
# ex) 1-10, 2-5, 6-8
# なら2-5, 6-8を選ぶ．
N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]
ab.sort(key=lambda x: x[1])
##print(ab)
ans = 1             # 一つ目分
tmp = ab[0][1] - 0.1      # 一つ目の橋は必ず壊すので
for i in range(1, M):
    if ab[i][0] < tmp < ab[i][1]:   # 直近で壊した橋が喧嘩している島の間にある時は何もしない
        pass
    else:                           # 間にない時は新しく橋を壊す
        ans += 1
        tmp = ab[i][1] - 0.1

print(ans)

'''
# ABC103D
# より簡潔な回答
N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]
ab.sort(key=lambda x: x[1])
ans = 1
tmp = ab[0][1]
for i in range(1, M):
    if tmp <= ab[i][0]:
        ans += 1
        tmp = ab[i][1]
print(ans)

'''