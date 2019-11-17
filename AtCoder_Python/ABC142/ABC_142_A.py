# ABC142B
N =  int(input())
if N % 2 == 0:
    ans = (N // 2) / N
else:
    ans = ((N + 1) // 2) / N
print("{:.10f}".format(ans))