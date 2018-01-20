""" Subarray Sum Equals K """

class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        ndic = {0:1}        
        total = 0
        for i in nums:
            total = total + i 
            if total-k in ndic:
                count += ndic[total-k]
            step = 0
            if total in ndic:
                step = ndic[total]
            ndic[total] = step + 1 
        return count
            
s = Solution()
print(s.subarraySum([-1,-1,1],1))
