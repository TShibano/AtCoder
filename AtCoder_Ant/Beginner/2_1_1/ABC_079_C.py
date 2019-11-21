# ABC079C
S = input()
# +を挿入するか-を挿入するかで全部で2 ** 3通り
for i in range(2**3):
    now_sum = int(S[0])
    for j in range(3):
        if (i >> j) & 1:
            now_sum += int(S[j+1])
        else:
            now_sum -= int(S[j+1])
    if now_sum == 7:
        ans = i
        break
fugo = ""
for j in range(3):
    if (ans >> j) & 1:
        fugo += "+"
    else:
        fugo += "-"

print("{}{}{}{}{}{}{}=7".format(S[0], fugo[0], S[1], fugo[1], S[2], fugo[2], S[3]))