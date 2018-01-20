""" Triangle """

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        dp = [triangle[0][0]]
        for i in range(1,len(triangle)):
            tmp = []
            for j in range(len(triangle[i])):
                if j == 0:
                    mincost = dp[0]+triangle[i][j]
                elif j == len(triangle[i])-1:
                    mincost = dp[-1]+triangle[i][j]
                else:
                    mincost = min(dp[j-1],dp[j])+triangle[i][j]
                tmp.append(mincost)
            dp = tmp

        return min(dp) 


s = Solution()
print(s.minimumTotal([[-1],[2,3],[1,-1,-3]]))                 
