h = [2,3,5,6]

# m = 0
#
# for i in range(len(h)):
#     for j in range(i, len(h)):
#         if h[i] >= h[j]:
#             if m < (j-i)*h[j]:
#                 m = (j-i)*h[j]
#         else:
#             if m < (j-i)*h[i]:
#                 m = (j-i)*h[i]
#
# print(m)

# brute force will exceed the time limit, should use two point approach, always count the smaller one

m = 0
l = 0
r = len(h)-1
while l < r:
    if m < min(h[l], h[r])*(r - l):
        m = min(h[l], h[r])*(r - l)
    if h[l] <= h[r]:
        l += 1
    else:
        r -= 1
    print(l,r)

print(m)
