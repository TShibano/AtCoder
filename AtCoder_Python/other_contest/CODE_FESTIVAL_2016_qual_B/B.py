# B
N, A, B = map(int, input().split())
S = input()

num_japan_student = 0
num_foreign_student = 0
ans_list = ["No"] * N
for i in range(N):
    if S[i] == 'a':
        num_japan_student += 1
        if num_japan_student + num_foreign_student <= A + B:
            ans_list[i] = "Yes"
    elif S[i] == 'b':
        num_foreign_student += 1
        if num_foreign_student <= B and num_japan_student + num_foreign_student <= A + B:
            ans_list[i] = "Yes"
        else:       # 海外学生が進めなかったら足したnum_foreignは減らす
            num_foreign_student -= 1
    else:
        pass

for i in range(N):
    print(ans_list[i])
