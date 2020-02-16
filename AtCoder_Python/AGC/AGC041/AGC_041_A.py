# AGC041A
N, A, B = map(int, input().split())
diff = B - A
if diff % 2 == 0:
    print(diff//2)
else:
    tmp1 = (B - A + 1) // 2
    tmp1 = B - tmp1
    tmp2 = (2 * N - B + A + 1) // 2 
    tmp2 = tmp2 - A
    print(min(N-A, B-1, tmp1, tmp2))
