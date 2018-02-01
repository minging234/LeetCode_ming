""" Longest Valid Parentheses """

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0]
        for i in range(1,len(s)):
            if s[i] == '(':
                dp.append(0)
            else:
                if i-dp[-1]-1 >= 0 and s[i-dp[-1]-1] == "(":
                    dp.append(dp[-1]+2)
                    if i-dp[-2]-2 > 0:
                        if s[i-dp[-2]-2] == ")":
                            dp[-1] += dp[i-dp[-2]-2]
                else:
                    dp.append(0) 
        return max(dp)

s = Solution()
print(s.longestValidParentheses("(()))())("))

