# ABC145B
N = int(input())
S = input()
if N % 2 == 1:
    print("No")
    exit()
for i in range(N//2):
    if S[i] == S[i + N // 2]:
        pass
    else:
        print("No")
        exit()
print("Yes")