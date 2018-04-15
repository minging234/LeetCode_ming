""" Maximum Subarray """

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [nums[0]]
        for i in range(1,len(nums)):
            dp.append(max(dp[-1]+nums[i],nums[i]))
        return max(dp)

            