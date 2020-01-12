# ABC151A
al=[chr(ord('a') + i) for i in range(26)]
C = input()
tmp = al.index(C)
print(al[tmp+1])