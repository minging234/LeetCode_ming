""" Unique Binary Search Trees """

class Solution(object):
    dic = {}
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 0 :
            return 1
        if n in self.dic:
            return self.dic[n]
        sum = 0
        for i in range(n):
            sum += self.numTrees(i) * self.numTrees(n-i-1)
        self.dic[n] = sum
        return sum

s =Solution()
print(s.numTrees(3))