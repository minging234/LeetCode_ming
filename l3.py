
s = "au"


outc = []
if not s:
    print(0)
q = ""
m = 0
for i in range(len(s)):
    if s[i] not in q:
        q = s[m:i + 1]
        print(q)
        outc.append(len(q))
    else:
        outc.append(len(q))
        m = m + q.index(s[i]) + 1
        q = s[m:i + 1]

print( max(outc))

print(s[0:2])