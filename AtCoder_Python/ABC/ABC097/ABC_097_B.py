# ABC097B
# ABC097-B
ans_list = [1]
for i in range(2, 10):
    ans_list.append(2 ** i)
for i in range(2, 7):
    ans_list.append(3 ** i)
for i in range(2, 5):
    ans_list.append(5 ** i)    
for i in range(2, 4):
    ans_list.append(6 ** i)
    ans_list.append(7 ** i)
    ans_list.append(10 ** i)
num = [11,12, 13, 14, 15, 17, 18, 19, 20, 21, 22,  23,24, 25, 26, 27, 28,  29, 30,  31]
for i in num:
    ans_list.append(i ** 2)
X = int(input())
for i in range(X, 0, -1):
    if i in ans_list:
        ans = i
        break
print(ans)
