# B
N = int(input())
i = 1
while 1:
    if i * (i-1) // 2 < N and N <= i * (i+1) // 2:
        max_ans = i
        break
    else:
        i += 1
not_use = max_ans * (max_ans+1) // 2 - N
for i in range(1, max_ans+1, 1):
    if i != not_use:
        print(i)