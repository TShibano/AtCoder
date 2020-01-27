# ABC084D
import bisect

def Get_Sieve_of_Eratosthenes(N):
    prime_list = [2]
    limit = int(N ** 0.5)
    numeric_data = [i for i in range(3, N, 2)]
    while True:
        prime = numeric_data[0]
        if prime >= limit:
            return prime_list + numeric_data
        prime_list.append(prime)
        numeric_data = [x for x in numeric_data if x % prime != 0]

def Get_2017_like_number(N, prime_list):
    ans_list = []
    for p in prime_list:
        if (p+1)//2 in prime_list:
            ans_list.append(p)
    return ans_list


def main():
    N = 10 ** 5
    prime_list = Get_Sieve_of_Eratosthenes(N)
    like_number_list = Get_2017_like_number(N, prime_list)

    # 入力
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]
    
    # 二分探索で見つける
    for q in Query:
        l = q[0]
        r = q[1]
        print(bisect.bisect_right(like_number_list, r) - bisect.bisect_left(like_number_list, l))

if __name__ == "__main__":
    main()


# 解説の解き方
# 素数判定リストの作成(True / False)
# 2017_like_number の個数リストの作成
# 累積和で獲得

N = 10**5
prime_list = [True] * (N+1)        # True が素数
count_list = [0] * (N+1)
for i in range(2, N+1, 1):
    if prime_list[i]:
        for j in range(i+i, N+1, i):
            prime_list[j] = False

for i in range(3, N+1, 2):
    if prime_list[i] and prime_list[(i+1)//2]:
        count_list[i] += 1

for i in range(3, N+1, 1):
    count_list[i] += count_list[i-1]

Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]
for q in query:
    l, r = q
    print(count_list[r] - count_list[l-1])