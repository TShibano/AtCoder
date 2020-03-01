N, K = map(int, input().split())

AB = []
for i in range(K):
    a, b = map(int, input().split())
    b -= 1
    AB.append([a, b])

# dp[day-1][pasta][cnt] := day 日目にpasta を食べる場合の数(cnt <= 2, 3はダメ)
dp = [[[0] * 3 for _ in range(3)] for __ in range(N+1)]
dp[0][0][0] = 1
AB.sort(key = lambda x: x[0])

i = 0   # 決まったパスタを食べる日を覚えておく変数
for day in range(1, N+1):
    if day == AB[i][0]:
        for pasta in range(3):
            if pasta == AB[i][1]:
                dp[day][pasta%3][1] += (dp[day-1][pasta%3][0] + 
                                        dp[day-1][(pasta+1)%3][0] + 
                                        dp[day-1][(pasta+1)%3][1] + 
                                        dp[day-1][(pasta+1)%3][2] + 
                                        dp[day-1][(pasta+2)%3][0]  + 
                                        dp[day-1][(pasta+2)%3][1] + 
                                        dp[day-1][(pasta+2)%3][2])

                dp[day][pasta%3][2] += dp[day-1][pasta%3][1]                
            else:
                for cnt in range(3):
                    dp[day][pasta][cnt] = 0
        # 決まったパスタを覚える変数の更新
        i += 1
        if i == K:
            i = 0
        continue

    else:
        for pasta in range(3):
            dp[day][pasta%3][1] += (dp[day-1][pasta%3][0] + 
                                    dp[day-1][(pasta+1)%3][0] + 
                                    dp[day-1][(pasta+1)%3][1] + 
                                    dp[day-1][(pasta+1)%3][2] + 
                                    dp[day-1][(pasta+2)%3][0] + 
                                    dp[day-1][(pasta+2)%3][1] + 
                                    dp[day-1][(pasta+2)%3][2])

            dp[day-1+1][pasta%3][2] += dp[day-1][pasta%3][1]

# 集計
ans = 0
for pasta in range(3):
    for cnt in range(3):
        ans += dp[N][pasta][cnt]

# 出力
print(ans%10000)
