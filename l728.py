
def selfDividingNumbers(left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    ans = []

    for i in range(left,right+1):
        if issdn(i) is True:
            ans.append(i)
    return ans



def issdn(num):
    t = num
    b = t % 10
    while t > 0:
        if b == 0:
            return False
        elif num%b != 0:
            return False
        t = int(t / 10)
        b = t % 10
    return True


print(selfDividingNumbers(1,22))