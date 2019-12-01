# ABC076C
# 方針：手前から決めていく
# Sにおいて?もしくはT[0]と一致するものがあれば見ていく
# 途中で一致しないものが出てくれば次の文字へ
# 置き換えれる部分は一番最後の部分だけTに置き換えてそれ以外の?はすべてaに置き換える
S = input()
T = input()
check = -1
for i in range(len(S) - len(T) + 1):
    if S[i] == "?" or S[i] == T[0]:
        k = 1
        flag = True
        while k < len(T):
            if S[i+k] == "?":
                k += 1
            else:
                if S[i + k] == T[k]:
                    k += 1
                else:       # 一致しない文字．例：S[i+T[k]]が?a?bcでTがdabzcの時四文字目が異なるのでダメ
                    flag = False
                    break
        if k == len(T) and flag == True:        # 条件に合致する時はその数字を覚える
            # 可能な数字があればどんどん更新していく
            check = i

if check != -1:
    S = list(S)
    for i in range(len(T)):
        S[check + i] = T[i]
    S = "".join(S)
    ans = S.replace("?", "a")
    print(ans)
else:
    print("UNRESTORABLE")