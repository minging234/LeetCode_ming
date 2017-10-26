
def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    i = 1
    a = '1'
    while i < n:
        j = 0
        s = ''
        c = 1
        while j < len(a):
            if j+1 == len(a):
                s = s + c.__str__() +a[j]

            elif a[j] != a[j+1]:
                s = s + c.__str__() +a[j]
                c = 1

            elif a[j] == a[j+1]:
                c += 1

            j += 1
        a = s
        i += 1
    return a


print(countAndSay(6))


