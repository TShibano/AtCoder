# ABC151E
# 組み合わせ(高速，フェルマーの小定理を利用)
def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
mod = 10**9+7 #出力の制限
N = 10 ** 5
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

mod = 10 ** 9 + 7
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ans_max = 0
ans_min = 0
# ans_minを求める
for i in range(N-K+1):
    ans_min += A[i] * cmb(N-1-i, K-1, mod)
    ans_min %= mod
for i in range(K-1, N):
    ans_max += A[i] * cmb(i, K-1, mod)
    ans_max %= mod
##print(ans_max, ans_min)
print((ans_max - ans_min + mod)%mod)