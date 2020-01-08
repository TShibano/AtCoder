# ABC123B
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

lst_result = []
lst = [[A, A % 10], [B, B % 10], [C, C % 10], [D, D % 10], [E, E % 10]]
lst_a = []
for i in range(len(lst)):
  if lst[i][1] == 0:
    lst_result.append(lst[i][0])
  else:
    lst_a.append(lst[i])

lst_a = sorted(lst_a, key = lambda x:x[1], reverse = True)


for i in range(len(lst_a)):
  lst_result.append(lst_a[i][0])

answer = 0
for i in range(len(lst_result)):
  if i < 4:
    if lst_result[i] % 10 == 0:
      answer += lst_result[i]
    else:
      tmp = lst_result[i] // 10 + 1
      answer += tmp * 10
  else:
    answer += lst_result[i]
print(answer)
