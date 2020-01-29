# ABC109D
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
check = [[False] * W for _ in range(H)]
now_flag = True     # True : Even, False : Odd
past_flag = True
ans = 0
ans_list = []
for h in range(H):
    if h % 2 == 0:
        for w in range(W):
            past_flag = now_flag
            now_flag = True if A[h][w] % 2 == 0 else False
            if not past_flag:      # odd
                now_flag = False if now_flag else True     # now is odd -> next is even
                ans += 1
                if h != 0 and w == 0:
                    ans_list.append([h, w+1, h+1, w+1])
                else:
                    ans_list.append([h+1, w, h+1, w+1])
    if h % 2 == 1:
        for w in range(W-1, -1, -1):
            past_flag = now_flag
            now_flag = True if A[h][w] % 2 == 0 else False
            if not past_flag:
                now_flag = False if now_flag else True
                ans += 1
                if h != 0 and w == W-1:
                    ans_list.append([h, w+1, h+1, w+1])
                else:
                    ans_list.append([h+1, w+2, h+1, w+1])

print(ans)
for a in ans_list:
    print(*a)
            