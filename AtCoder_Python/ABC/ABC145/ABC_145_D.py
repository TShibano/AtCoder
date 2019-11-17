# ABC145D
def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

X, Y = map(int, input().split())

if X % 3 == 1 and Y % 3 == 1:
    print(0)
    exit()
if X % 3 == 2 and Y % 3 == 2:
    print(0)
    exit()

a = 2 * Y // 3 - X // 3
b = 2 * X // 3 - Y // 3


mod = 10**9+7 #出力の制限
N = a + b + 3
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

print(cmb(a+b, b, mod))