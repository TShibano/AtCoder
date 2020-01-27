# ABC153D
H = int(input())
for i in range(60):
    if 2 ** i > H:
        print(2 ** i - 1)
        exit()
