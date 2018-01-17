"""K Inverse Pairs Array"""

class Solution:
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # dp = [[0] for i in range(3)] 
        # if I want to initial a two demention list, I could use the above method to aviod shallow copy
        dp = [0] * (k+1)
        for i in range(n+1):
            if i == 0:
                dp[0] = 1
                continue
            tmp = []
            for j in range(k+1):
                if j == 0:
                    tmp.append(1)
                    continue
                item = 0
                # for p in range(min(i-1,j)+1):
                #     item += dp[j-p]
                # ----- the common dp way -----
                if j-i >= 0:
                    val = dp[j] - dp[j - i]
                else:
                    val = dp[j]
                item = tmp[-1]+ val 
                
                tmp.append(item % 1000000007)
            dp = tmp
            # print (tmp)
        return dp[-1]



a = Solution()
b = a.kInversePairs(3,2)
print(b)