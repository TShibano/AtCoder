# ABC044B
w = input()
ww = sorted(w)
flag = True
if len(w) % 2 != 0:
    flag = False
else:
    ww = sorted(w)
    for i in range(0, len(ww), 2):
        if ww[i] != ww[i+1]:
            flag = False
        
if flag:
    print("Yes")
else:
    print("No")

# 愚直解
w = input()
a = w.count("a") % 2
b = w.count("b") % 2
c = w.count("c") % 2
d = w.count("d") % 2
e = w.count("e") % 2
f = w.count("f") % 2
g = w.count("g") % 2
h = w.count("h") % 2
i = w.count("i") % 2
j = w.count("j") % 2
k = w.count("k") % 2
l= w.count("l") % 2
m = w.count("m") % 2
n = w.count("n") % 2
o = w.count("o") % 2
p = w.count("p") % 2
q = w.count("q") % 2
r = w.count("r") % 2
s = w.count("s") % 2
t = w.count("t") % 2
u = w.count("u") % 2
v = w.count("v") % 2
W = w.count("w") % 2
x = w.count("x") % 2
y= w.count("y") % 2
z = w.count("z") % 2

if(a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p + q + r + s+ t + u + v + W + x + y + z)== 0:
    print("Yes")
else:
    print("No")
