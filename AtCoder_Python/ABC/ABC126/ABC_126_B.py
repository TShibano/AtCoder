# ABC126B
#B問題
if "00" < S[0:2] <="12" and "13" <= S[2:4] <= "99":
    print("MMYY")
elif "13" <= S[0:2] <= "99" and "00" <S[2:4] <= "12":
    print("YYMM")
elif "00" < S[0:2] <= "12" and "00" < S[2:4] <= "12":
    print("AMBIGUOUS")
elif "00" == S[0:2] and "00" < S[2:4] <= "12":
    print("YYMM")
elif "00" < S[0:2] <= "12" and S[2:4] == "00":
    print("MMYY")
else:
    print("NA")
