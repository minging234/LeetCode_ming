""" Climbing Stairs """

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        dp = []
        dp.append(1)
        dp.append(2)
        for i in range(2,n):
            dp.append( dp[i-1] + dp[i-2] )
        return dp[-1]