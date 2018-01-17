class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
    
        i = 0
        while i < len(nums):
            j = i
            ssum = 0
            while j < len(nums)-i:
                ssum = ssum + j
                if k == 0 and ssum == 0 and j > i:
                    return True
                elif k != 0 and ssum % k == 0 and j > i:
                    return True
                j += 1
            i += 1
        return False




