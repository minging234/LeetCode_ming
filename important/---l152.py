""" Maximum Product Subarray """

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = maxp = minp = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < 0:
                maxp, minp = minp, maxp
            maxp = max(nums[i], maxp * nums[i])
            minp = min(nums[i], minp * nums[i])
            r = max(r,maxp)
        return r





