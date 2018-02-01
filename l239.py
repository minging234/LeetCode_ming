""" Sliding Window Maximum """

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        ans = []
        i = k
        while i + k - 1 < len(nums):
            ans.append(max(nums[i:i+k]))
            i += 1
        return ans

