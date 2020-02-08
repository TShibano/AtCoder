# ABC125B
N = int(input())
V_lst = list(map(int, input().split()))
C_lst = list(map(int, input().split()))


P_lst = []
for i in range(N):
    P_lst.append(V_lst[i] - C_lst[i])
    
ans = 0    
for i in range(N):
    if P_lst[i] > 0:
        ans += P_lst[i]
        
print(ans)        
