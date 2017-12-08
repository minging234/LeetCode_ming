# dci = {}
# dci["a"]=[1,2,3]
# print(dci["a"])

a = [1,2,3,3,4]
# a[0],a[1] = a[1], a[0]
print(a)

pos = a.index(4)
while a[pos] <= val:
    pos -= 1
