# class Solution(object):

def findPoisonedDuration(timeSeries, duration):
    """
    :type timeSeries: List[int]
    :type duration: int
    :rtype: int
    """
    last = 0

    l = 0

    for i in range(len(timeSeries)):
        if i < len(timeSeries)-1:
            if timeSeries[i+1] > timeSeries[i] + duration:
                pice = timeSeries[i] - timeSeries[l] + duration
                l = i+1
            else:
                pice = 0
        else:
            pice = timeSeries[i] - timeSeries[l] + duration
        # print(i,timeSeries[i],tag,pice)
        last = last + pice

    return last


time = [1,3,5,7,9,11,13,15]
dur = 3

print(findPoisonedDuration(time,dur))