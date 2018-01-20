""" Russian Doll Envelopes """

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        envelopes.sort()
        put = [1]
        ans = 1
        for i in range(1,len(envelopes)):
            putlen = 1
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    putlen = max(putlen, put[j]+1)
            put.append(putlen)
            ans = max(ans, putlen)
        return ans
                
s = Solution()
print(s.maxEnvelopes([[10,8],[1,12],[6,15],[2,18]]))


""" 超时了，还没有想出来怎么改进 """
        
