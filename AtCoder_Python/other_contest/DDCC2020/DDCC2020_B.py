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

N = int(input())
A = list(map(int, input().split()))
A = np.array(A)
sum_A = np.sum(A)
res = np.cumsum(A)
value = getNearestValue(res, sum_A/2)
print(abs(value - (sum_A - value)))
