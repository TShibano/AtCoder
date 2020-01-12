# ABC080B
N = input()
l = len(N)
fn = 0
for i in range(l):
    fn += int(N[i])
if int(N) % fn == 0:
    print('Yes')
else:
    print('No')
