"""Kth Largest Element"""

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums, reverse=True)[k-1]


