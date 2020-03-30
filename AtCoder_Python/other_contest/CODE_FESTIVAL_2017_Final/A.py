# A
ans_string = "AKIHABARA"
n = len(ans_string)

S = input()
ans_list = ["AKIHABARA", "AKIHABAR", "AKIHABRA", "AKIHABR", 
            "AKIHBARA", "AKIHBAR", "AKIHBRA", "AKIHBR", 
            "KIHABARA", "KIHABAR", "KIHABRA", "KIHABR", 
            "KIHBARA", "KIHBAR", "KIHBRA" ,"KIHBR"
            ]
if S in ans_list:
    ans = "YES"
else:
    ans = "NO"
print(ans)