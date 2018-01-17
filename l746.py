""" Min Cost Climbing Stairs """

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        far = 0
        clo = 0

        for i in range(2,len(cost)+1):
            pre = clo
            clo = min(far + cost[i-2], clo + cost[i-1])
            far = pre

        return clo