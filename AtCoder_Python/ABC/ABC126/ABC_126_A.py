# ABC126A
#A問題
N, K = map(int, input().split())
S = input()
S_lst = list(S)
if S_lst[K-1] == "A":
    S_lst[K-1] = "a"
    print("".join(S_lst))
elif S_lst[K-1] == "B":
    S_lst[K-1] = "b"
    print("".join(S_lst))
else:
    S_lst[K-1] = "c"
    print("".join(S_lst))
