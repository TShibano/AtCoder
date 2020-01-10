# ABC052B
N = int(input())
S = input()
x_lst = [0]
x = 0
for i in range(N):
    if S[i] == "I":
        x += 1
    else:
        x -= 1
    x_lst.append(x)
print(max(x_lst))
