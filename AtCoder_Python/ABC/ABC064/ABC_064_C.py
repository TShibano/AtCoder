# ABC064C
# C
import collections
N = int(input())
a = list(map(int, input().split()))
def color(rate):
    if 1 <= rate <= 400:
        return 'gray'
    elif 400 <= rate < 800:
        return 'brown'
    elif 800 <= rate < 1200:
        return 'green'
    elif 1200 <= rate < 1600:
        return 'mizu'
    elif 1600 <= rate < 2000:
        return 'blue'
    elif 2000 <= rate < 2400:
        return 'yellow'
    elif 2400 <= rate < 2800:
        return 'orange'
    elif 2800 <= rate < 3200:
        return 'red'
    else:
        return 'change'
color_lst = []
change_num = 0
for i in range(N):
    tmp = color(a[i])
    if tmp == 'change':
        change_num += 1
    else:
        color_lst.append(tmp)
color_counter = collections.Counter(color_lst)
num = color_counter.keys()
if len(num) != 0:
    print('{} {}'.format(len(num), len(num) + change_num))
else:
    print('{} {}'.format(1, change_num))
