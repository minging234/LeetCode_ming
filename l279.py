""" Perfect Squares """

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append( i * i )
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y)
            toCheck = temp

        return cnt




s = Solution()
print(s.numSquares(7691))



"""
    DFS 超时了，很明显，这道题不应该搜索所有的情况
        
        ndic = {1:1}
        
        def dfs(num):
            if num == 0:
                return 0
            if num in ndic:
                return ndic[num]
            r = int(num**0.5)
            a = num
            for i in range(r,0,-1):
                a = min(a, dfs(num - i**2)+1)
            ndic[num] = a
            return a

        return dfs(n)

    一种考虑是使用BFS，只找到最浅的到达0的路径就可以了



"""