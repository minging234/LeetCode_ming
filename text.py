# dci = {}
# dci["a"]=[1,2,3]
# print(dci["a"])

# a = [1,2,3,3,4]
# # a[0],a[1] = a[1], a[0]
# print(a)

# pos = a.index(4)
# while a[pos] <= val:
#     pos -= 1

# g = "a"
# d = "b"

# print(g < d)

# def tonum(time):
#     return int(time[2:])*60 + int(time[3:])

# # print(tonum("02:01"))

# time  = "02:01"
# print(int(time[:2]))
# print(int(time[3:]))

# a = 'abca'
# print(a.count("a"))


# a = [None]
# if a :
#     print ("hahah")
# print(a)

# a = [1,2,3,None,None]
# if None in a:
#     a.remove(None)

# print(a)

# dic = {1:2,2:3,3:1,4:2}
# print(dic.items())

# for i in dic.items():
#     print(i) 

# a = sorted(dic.items(),key = lambda b: b[1],reverse=True)
# print(a)

# a = 1000000
# print (len(str(bin(a))))
# a = 5 & 0
# b = 5
# c = b >> 1
# print(a,c)

# import collections
# a = collections.Counter("abncsad")
# print(a)
# a = collections.Counter([5,1,2,3,4,1,2,3])
# print(a)

# for i in range(2,1):
#     print(i)


# a = [[1,2], [2,3], [3,4],[2,6],[6,8],[4,5]]
# print (sorted(a))

# b= float('-inf')
# if b < 0:
#     print (b)

# a = [1,2,3,4,5,6]
# print(a[8:])


# a = [[1,2,3], [4,5,6]]
# print (a)
# print (map(list, zip(*a)))    
# print (list(map(list, zip(*a))))


# a = int(4/3)
# b = 4%4
# print (b)

# a = [[1,2,3], [4,5,6]]
# print (1 in a)

# a = [1,2,3]
# print(1 in a[4:])

# for i in range(1,0):
#     print(i)

# a = ["1","2","3"]
# b = list(a) 
# b.remove("1")
# print(a,b)

# a = [1,2,4,3]
# a.sort()
# print(a)

# dic = {1:0}
# dic.pop(1,None)
# print (dic)

# a = "abcdefg"

# print(a[::1])

# t = []
# b = list(t)
# print(b)

# a = 'abcd'
# a[2] = 'a'

# print(a)

# a = list(range(1,1))
# print(a)

# a = []
# a.append(None)

# print (a)

# target = 3
# su = [1,5,11,5]

# dp =[[False] * target] * len(su)

# print(dp)

# for i in dp:
#     i = True
# print(dp)

# a = []
# print(a[-1])

# board = [[4,1,2],[5,0,3]]
# bd = list(board)
# b = 1
# bd[b][0],bd[b][1] = bd[b][1],bd[b][0]

# print(board,bd)

# a = "9"
# b = "a"

# print(a>b)

# a = 123
# print(list(str(a)))

# a = [1,2,3,4,5,5,5,5,5,5,5,6]
# # for i, cand in enumerate(a):
# #     print(i,cand)

# import bisect

# b = bisect.bisect_right(a,5)
# c = bisect.bisect_left(a,5)
# print(b,c)

# a = [1,2,3,4,5]

# import collections

# b = collections.Counter(a)

# print(b)

# a = [1,2,3,4,5,6,7,8,9,10]

# print(a[-5:])

# a = [1,2,3,4,1,1,1]
# import collections

# b = collections.Counter(a)

# print(b[5])

# a = {}
# l ='a'
# a [l] = [1,2,3]
# print(a[l])

# a = -3
# # b = a % 5
# # print(b)

# b = 'f'
# a = int(b,16)
# print (a)

print(ord("a"))