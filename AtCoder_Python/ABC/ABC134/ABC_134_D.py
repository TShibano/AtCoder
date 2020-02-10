# ABC134D
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

N = int(input())
A = list(map(int, input().split()))
cnt_list = [0] * N
M = 0
ans_list = []
for i in range(N-1, -1, -1):
    if A[i] == 1 and cnt_list[i] % 2 == 0:
        M += 1
        ans_list.append(i+1)
        tmp_list = make_divisors(i+1)
        for t in tmp_list:
            cnt_list[t-1] += 1
    elif A[i] == 1 and cnt_list[i] % 2 == 1:
        pass
    elif A[i] == 0 and cnt_list[i] % 2 == 0:
        pass
    else:
        M += 1
        ans_list.append(i+1)
        tmp_list = make_divisors(i+1)
        for t in tmp_list:
            cnt_list[t-1] += 1
print(M)
if M == 0:
    exit()
print(" ".join(map(str, ans_list)))