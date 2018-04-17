class Solution:
    def longestcommon(s,p):
        dp = [0]*len(s)
        for i in range(1,len(p)):
            temp = [0]
            for j in range(1,len(s)):
                if s[i] = s[j]:
                    temp.append(dp[j-1]+1)
                else:
                    temp.append(max(temp[-1],dp[j]))
            dp = temp
    
    return dp[-1]

