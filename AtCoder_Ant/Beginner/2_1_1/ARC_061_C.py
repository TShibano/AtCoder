# ARC061C
S = input()
N= len(S)
ans = 0

# +を挿入するのは2 ** (N-1)．間に入れるか入れないか
for i in range(2 ** (N - 1)):
    # iは各桁に+を挿入するかどうかを決定する．2進数として考える
    now_sum = 0                 # i番目の和を考える
    reg = int(S[0])
    for j in range(N - 1):      # 0or1を調べるためのループ
        if i & (1 << j):        # j回シフトした1とiの論理積をとることで1かどうかを調べる
      # if (i >> j) & 1:        # でも可．iをj回右シフトして，1と論理積をとる(最下位が1かを調べる) 
            now_sum += reg      # 1ならi番目の和にregを足す
            reg = 0
        reg *= 10               # 1でないならreg * 10 する.reg = 12なら120にする
        reg += int(S[j + 1])    # そして120 + 3で123となる
    now_sum += reg
    ans += now_sum
 
print(ans)