""" Edit Distance """

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m,n = len(word1),len(word2)
        dp = []
        for i in range(m+1):
            dp.append(i)
        
        for j in range(1,n+1):
            tmp = [j]
            for i in range(1,m+1):
                if word1[i-1] == word2[j-1]:
                    tmp.append(dp[i-1])
                else:
                    tmp.append(min(dp[i-1]+1,dp[i]+1,tmp[-1]+1))
            dp = tmp

        return dp[-1]

s = Solution()
print(s.minDistance("sea","ate"))


