# ABC097A
a, b, c, d = map(int, input().split())
if d >= abs(c-a):
    ans = "Yes"
else:
    if d >= abs(b-a) and d >= abs(c-b):
        ans = "Yes"
    else:
        ans = "No"
print(ans)        