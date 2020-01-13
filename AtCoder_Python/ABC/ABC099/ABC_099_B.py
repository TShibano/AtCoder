# ABC099B
a, b = map(int, input().split())
k = b - a - 1   # 西側の塔の位置
ans = k * (k + 1) // 2 - a
print(ans)
