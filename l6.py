s = 'shdfakdfhas'
r = 4


q = []
for i in range(r):
    q.append("")

cur = 0
direct = 1

while len(s) > 0:
    q[cur] += s[0]
    print(q[cur])
    s = s[1:]
    cur = cur + direct
    if cur ==r or cur <0:
        direct = - direct
        cur  = cur + 2* direct


print(q)


