S = input()
if len(S) < 4:
    ans = "No"
else:
    if S[0:4] == "YAKI":
        ans = "Yes"
    else:
        ans = "No"
print(ans)