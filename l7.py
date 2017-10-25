pc = []
t = x
outc = 0

flag = 0
if t < 0:
    flag = 1
    t = -t
while t > 0:
    p = t % 10
    t = int(t / 10)
    pc.append(p)

for i in pc:
    outc = 10 * outc + i

if flag == 1:
    outc = -outc
l = -2 ** 31
h = 2 ** 31 - 1
print(h)
if outc < l or outc > h:
    print(0)
print(outc)