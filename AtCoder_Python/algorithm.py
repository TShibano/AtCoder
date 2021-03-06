# リストのコピーは気をつけて
import copy 
original_list = [1, 2, 3]
copy_list = copy.deepcopy(original_list)

# リストの個数列挙
import collections
lst = [1, 2, 2, 3, 3]
c = collections.Counter(lst)
c.most_common()[0][0]   # 最も多い個数の要素
c.most_common()[0][1]   # 最も多い個数

# 約数列挙
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

# リスト転置
a_t = [list(x) for x in zip(*a)]

# 二重ソート
# 0列目に対してそーと
# 1列目に対して逆順ソート(整数のみか？)
lst = [[1, 2, 3], [4, 5, 6]]
lst.sort(key=lambda x:(x[0], -x[1]))

#アルファベット
al=[chr(ord('a') + i) for i in range(26)]
print(al)

# 最小公倍数
from fractions import gcd
from functools import reduce
def lcm (x, y):
    return (x * y) // gcd(x, y)

# 最小公倍数(リスト)
def lcm_list(numbers):
    return reduce(lcm, numbers, 1)

# 公約数のリスト獲得
def cf(X, Y):
    ans = [1]
    for i in range(2, min(X, Y) + 1):
        if X % i == 0 and Y % i == 0:
            ans.append(i)
    return ans

# リストの最大公約数
import math
import functools

def gcd_list(num_list):
    return functools.reduce(math.gcd, num_list)


# 素数判定
import math
def is_prime(N):
    if N == 1:
        return False
    for k in range(2, int(math.sqrt(N)) + 1):
        if N % k == 0:
            return False
    return True

# deque <- queueの代わりに使う
from collections import deque
que = deque()
que.append(1)       # 末尾に追加
que.popleft(1)      # 先頭を削除
que[0]

que.appendleft(1)   # 先頭に追加
que.pop()           # 末尾を削除

# heapqについて
import heapq
lst = [1, 6, 8, 0, -4]
heapq.heapify(lst)      # リストを優先度付きキューへ
heapq.heappop(lst)      # 最小値の取り出し  O(log N)
heapq.heappop(lst, -2)  # 要素の挿入
# 最大値の取り出しはリストの各要素にマイナス1をかけた上で最小値として取り出す



# 素因数分解
def prime_factorization(N):
    tmp = N
    ans = []
    for i in range(2, int(N ** 0.5) + 1):
        count = 0
        while tmp % i == 0:
            tmp //= i
            count += 1
        if count != 0:
            ans.append([i, count])
    if tmp != 1:
        ans.append([tmp, 1])
    if ans == []:
        ans.append([N, 1])
    return ans

# 桁数獲得
def get_keta(N):
    ans = 1
    while True:
        if N // 10 != 0:
            ans += 1
            N //= 10
        if N // 10 == 0:
            break
    return ans


# 階乗
import math 
math.factorial(10)

# 順列全列挙
import itertools
all_permutation_list = itertools.permutations(lst)
partial_permutation_list = itertools.permutations(lst, r=2)  # 長さ2の順列を返す

# 順列の全ての長さにおけるパターンを出したい時
all_all_permutation_list = []
for i, _ in enumerate(lst, 1):
    for tmp_list in itertools.permutations(lst, r=i):
        all_all_permutation_list.append(tmp_list)

# 組み合わせ
from scipy.misc import comb         # AtCoder用
from scipy.special import comb      # 普段用

# 組み合わせ(高速，フェルマーの小定理を利用)
def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
mod = 10**9+7 #出力の制限
N = 10 ** 4
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

# 組み合わせ(N > 10 ** 7 でも可能)
def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def comb(n, r, p):
    ret = 1
    while 1:
        if (r == 0):
            break
        N = n % p
        R = r % p
        if N < R:
            return 0
        for i in range(R):
            ret = ret * (N-i) % p
        imul = 1
        for i in range(R):
            imul = imul * (i+1) % p
        ret = ret * modinv(imul, p) % p
        n //= p
        r //= p
    return ret




# リストを空白出力
lst = [1, 2, 3]
print(" ".join(map(str, lst)))

# 累積和獲得
import numpy as np
a = [1, 4, 10]
res = np.cumsum(a)
# res = [1, 5, 15]

# set演算子
a = set(1, 2, 3)
b = set(2, 3, 4)
union_a_b = a | b   # 和集合
union_a_b = a.union(b)  # 和集合
intersection_a_b = a & b    # 積集合
intersection_a_b = a.intersection(b)    # 積集合

import numpy as np
def getNearestValue(list, num):
    """
    概要: リストからある値に最も近い値を返却する関数
    @param list: データ配列
    @param num: 対象値
    @return 対象値に最も近い値
    """

    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    idx = np.abs(np.asarray(list) - num).argmin()
    return list[idx]


# リスト表示
for a in lst:
    print(*a)

# リストの要素の個数について
import collections
lst = [1, 1, 1, 2, 2, 3, 4, 5, 6,]
c = collections.Counter(lst)
c.most_common()[0][0]   # lstの要素の内，最も個数が多いものの値
c.most_common()[0][1]   # lstの要素の内，最も個数が多い物の個数


# 二分探索
import bisect
lst = [1, 4, 8, 14, 25]
a = 10
bisect.bisect_left(lst, a)  # 3 (14のところ)
bisect.bisect_right(lst, a) # 3 (14のところ)

lst = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3]
a = 1
bisect.bisect_left(lst, a)  # 3
bisect.bisect_right(lst, a) # 7


# 文字列
s = "abcd"
s = s.capitalize()  # s = "Abcd"


# 素数リストを獲得(エラトステネスの篩, O(NloglogN) )
def Get_Sieve_of_Eratosthenes(N):
    prime_list = [2]
    limit = int(N ** 0.5)
    numeric_data = [i for i in range(3, N, 2)]
    while True:
        prime = numeric_data[0]
        if prime >= limit:
            return prime_list + numeric_data
        prime_list.append(prime)
        numeric_data = [x for x in numeric_data if x % prime != 0]


# ランレングス圧縮 Run Length Encoding
def RanLengthEncoding(S):
    N = len(S)
    RLE = []
    now_char = S[0]
    now_cnt = 1
    for i in range(1, N):
        if now_char == S[i]:
            now_cnt += 1
        else:
            RLE.append([now_char, now_cnt])
            now_char = S[i]
            now_cnt = 1
    RLE.append([now_char, now_cnt])
    return RLE