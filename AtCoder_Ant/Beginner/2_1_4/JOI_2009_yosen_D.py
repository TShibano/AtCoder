# JOI2009D
# 全列挙
import itertools
N = int(input())
K = int(input())
card_list = [input() for _ in range(N)]

ans = 0
create_card_list = []       # 作った数字を入れるところ

# パターンを全列挙
k_permutation_list = itertools.permutations(card_list, K)

for lst in k_permutation_list:
    tmp = int("".join(lst))         # 数字を作成
    if tmp not in create_card_list:     # 作ったかどうかを確認
        create_card_list.append(tmp)
        ans += 1

print(ans)