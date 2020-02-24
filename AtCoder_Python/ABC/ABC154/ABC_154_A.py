# ABC154A
S, T = map(str, input().split())
A, B = map(int, input().split())
U = input()
if S == U:
    print(A-1, B)
elif T == U:
    print(A, B-1)
else:
    print(A, B)
