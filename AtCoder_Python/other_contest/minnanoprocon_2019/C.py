# C
K, A, B = map(int, input().split())
if A >= B:
    print(K + 1)
    exit()

# A - 1 回叩いて A 枚にする
# 残り K - (A - 1) 回については，A 枚を1 円にして，B 枚のクッキーに増やすを繰り返す．
tmp = K - (A - 1)
if tmp < 0:
    print(K + 1)
    exit()
cnt = tmp // 2
amari = tmp % 2

ans = cnt * B - (cnt - 1) * A + amari
ans = max(ans, K + 1)
print(ans)