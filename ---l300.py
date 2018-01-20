""" Longest Increasing Subsequence """

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        ans = 0
        for i in range(len(nums)):
            vmax = 1
            for j in range(i):            
                if nums[i] > nums[j]:
                    vmax = max(vmax,dp[j] + 1 )
            ans = max(ans,vmax)
            dp.append(vmax)
        return ans


s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))

"""         
    不使用dp也是最快的方法    
        n = len(nums)
        if n <= 1:
            return n
        
        tail = []
        for num in nums:
            if len(tail) == 0 or num > tail[-1]:
                tail.append(num)
            elif num < tail[0]:
                tail[0] = num
                
            else:
                idx = bisect.bisect_left(tail, num)
                tail[idx] = num
                
        return len(tail)
"""
