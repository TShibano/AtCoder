# ABC111C
# ABC111C
import collections

n = int(input())
v = list(map(int, input().split()))
if len(set(v)) == 1:
    print(n//2)
    exit()

v_odd = [0] * (n // 2)
v_even = [0] * (n // 2)
for i in range(n):
    if (i+1)%2 == 1:
        v_odd[i//2] = v[i]
    else:
        v_even[i//2] = v[i]
c_v_odd = collections.Counter(v_odd)
c_v_even = collections.Counter(v_even)

if c_v_odd.most_common()[0][0] == c_v_even.most_common()[0][0]:
    if c_v_odd.most_common()[0][1] > c_v_even.most_common()[0][1]:
        odd_count = n//2 - c_v_odd.most_common()[0][1]
        even_count = n//2 - c_v_even.most_common()[1][1]
        ans = odd_count + even_count
    elif c_v_odd.most_common()[0][1] < c_v_even.most_common()[0][1]:
        odd_count = n//2 - c_v_odd.most_common()[1][1]
        even_count = n//2 - c_v_even.most_common()[0][1]
        ans = odd_count + even_count
    else:
        if c_v_odd.most_common()[1][1] > c_v_even.most_common()[1][1]:
            odd_count = n//2 - c_v_odd.most_common()[1][1]
            even_count = n//2 - c_v_even.most_common()[0][1]
            ans = odd_count + even_count
        else:
            odd_count = n//2 - c_v_odd.most_common()[0][1]
            even_count = n//2 - c_v_even.most_common()[1][1]
            ans = odd_count + even_count
else:
    odd_count = n//2 -  c_v_odd.most_common()[0][1]
    even_count = n//2 -  c_v_even.most_common()[0][1]
    ans = odd_count + even_count
print(ans)