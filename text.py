# s = "hadhfsdp"
# d = []
# for i in range(len(s)):
#     d.append(s[i])
#
#
# def getchar(st):
#     c = st.pop()
#     if c == "*":
#         c = getchar(st)
#     return c
#
#
# def tostring(s, p):
#     a = ""
#     b = ""
#     for i in range(len(s)):
#         a = a + s[i]
#     for j in range(len(p)):
#         b = b + p[j]
#     return a, b
#
# e = ["a","c"]
#
# print(d,e)
#
# m, n = tostring(d, e)
# print(m,n)

# c = getchar(d)
# print(c)

# d.reverse()
# print(d)



# a = ["a","b","c","d","e","f"]
#
# b = a[0:3]
# print(b)

# a = "ab"
# for i in range(0):
#     print(i)

# a = [4,3,2,3,1,3,2,4,2]
# b = [1,2,1,3,4,3,2,4]
#
# print(a[1:])


a = {}
a[1] = "ha"
a[2] = "bu"

print(a)


#
# def melon_count(boxes, melons):
#     b = list(reversed(melons))
#     sbox = sorted(boxes)
#     num1 = 0
#     num = 0
#     la = 0
#     for i in melons:
#         (a, w) = binary_s(sbox, i)
#         if a is not False and w > la:
#                 sbox.remove(a)
#                 num += 1
#                 la = w
#         else:
#             break
#     la = 0
#
#     for i in b:
#         a,w = binary_s(sbox, i)
#         print(a, w )
#         if a is not False and w < la:
#             sbox.remove(a)
#             num1 += 1
#             la = w
#         else:
#             break
#     print(num1, num)
#     if num1 > num:
#         return num1
#     else:
#         return num
#
#
# def binary_s(alist, iterm):
#     first = 0
#     last = len(alist) - 1
#     while first <= last:
#         midpoint = (first + last) // 2
#         if alist[midpoint] < iterm:
#             first = midpoint + 1
#         elif alist[midpoint] > iterm:
#             last = midpoint - 1
#         elif alist[midpoint] == iterm:
#             return alist[midpoint], first
#     if first < len(alist) - 1:
#         return alist[first],first
#     else:
#         return False
#
# print(melon_count(a,b))


# def melon_count(boxes, melons):
#     melonsr = list(reversed(melons))
#     boxesr = list(reversed(boxes))
#     flag = True
#     for i in range(len(melons)):
#         for j in range(len(boxes)):
#             if melons[i] <= boxes[j]:
#                 boxes = boxes[j+1:]
#                 break
#             flag = False
#             num1 = i+1
#         if flag == False:
#             break
#
#     for i in range(len(melonsr)):
#         for j in range(len(boxesr)):
#             if melonsr[i] <= boxesr[j]:
#                 boxesr = boxesr[j+1:]
#                 break
#             num2 = i+1
#             flag = False
#         if flag == False:
#             break
#
#     if num1 > num2:
#         return num1
#     else:
#         return num2
#
#
#
# print(melon_count(a,b))


