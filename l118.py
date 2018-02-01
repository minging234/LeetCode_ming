""" Pascal's Triangle """

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        if numRows == 0:
            return ans
        each = [1]
        ans.append(each)
        while len(ans) < numRows:
            tmp = [] 
            for i in range(len(each)+1):
                if i == 0:
                    tmp.append(each[0])
                elif i == len(each):
                    tmp.append(each[-1])
                else:
                    tmp.append(each[i-1]+each[i])
            ans.append(tmp)
            each = tmp

        return ans

s = Solution()
print(s.generate(5))