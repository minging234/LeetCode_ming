""" Unique Paths """

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        total = m + n - 2
        move = min(m,n) -1

        u = 1
        d = 1

        for i in range(move):
            u *= total
            total -= 1
            d *= i+1

        return int(u/d)

s = Solution()
print(s.uniquePaths(7,3))