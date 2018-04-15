""" Search for a Range """

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        import bisect
        l = bisect.bisect_left(nums,target)
        r = bisect.bisect_right(nums,target)
        if l == r:
            return [-1,-1]
        return [l,r-1]