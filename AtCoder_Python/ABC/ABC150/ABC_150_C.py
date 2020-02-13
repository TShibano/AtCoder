# ABC150C
import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

A = [i+1 for i in range(N)]
all_permutation_list = list(itertools.permutations(A))
a = all_permutation_list.index(P)
b = all_permutation_list.index(Q)
print(abs(a - b))