class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def tonum(time):
            return int(time[:2])*60 + int(time[3:])
        a = list(map(tonum,timePoints))
        a.sort()
        diff = 24*60+a[0]-a[-1]
        for i in range(1,len(a)):
            diff = min(diff, a[i]-a[i-1])
        return diff 
