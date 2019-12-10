# ABC147B
def palindrome(string): return True if string==string[::-1] else False

S = input()
ans = 0
if len(S) % 2 == 0:
    for i in range(len(S) // 2):
        if S[i] == S[-i-1]:
            pass
        else:
            ans += 1
else:
    for i in range(len(S) // 2):
        if S[i] == S[-i-1]:
            pass
        else:
            ans += 1
print(ans)