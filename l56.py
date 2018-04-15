""" Merge Intervals """

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals = sorted(intervals, key =lambda itv: itv.start)
        sta = intervals[0].start
        end = intervals[0].end
        ans = []

        for i in range(1,len(intervals)):
            if intervals[i].start <= end:
                end = max(end, intervals[i].end)
            else:
                ans.append(Interval(sta,end))
                sta = intervals[i].start
                end = intervals[i].end

        ans.append(Interval(sta,end))
        return ans