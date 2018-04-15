""" Target Sum """

class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = [0]*2001
        dp[nums[0]+1000] = 1
        dp[-nums[0]+1000] += 1
        for i in range(1,len(nums)):
            temp = [0]*2001
            for j in range(2001):
                if dp[j] > 0:
                    temp[j+nums[i]] += dp[j]
                    temp[j-nums[i]] += dp[j]
            dp = temp
        return dp[S+1000] if S<1000 else 0





"""

    brute force 的方法，显然超时了
        l = len(nums)
        self.ans = 0

        def dfs(ind, n):
            if ind == l:
                if n == 0:
                    self.ans += 1
                return
            dfs(ind+1,n+nums[ind])
            dfs(ind+1,n-nums[ind])
            return
        
        dfs(0,S)
        return self.ans

    大神的牛逼方法，将问题转化为单纯的求子序列的和为target 的dp问题

        # two subsets, plus and minus
        # plus - minus = S
        # plus + minus = sum(nums)
        # so plus = (S + sum(nums))/2
        
        total = sum(nums)
        
        if (S+total)%2:
            return 0
        
        if S > total:
            return 0
        
        target = (S+total) // 2
        # the problem now becomes, find ways to sum the subarrays that equals target
        # now a dp problem
        
        ret = [0] * (target+1)
        ret[0] = 1
        for num in nums:
            for i in range(target, num-1, -1):
                # this makes sure we don't sum twice
                ret[i] += ret[i-num]

        return ret[target]
        
"""