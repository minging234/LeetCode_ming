""" Number of Islands """

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        sdic = {}
        count = 0
        w = len(grid)
        h = len(grid[0])

        def search(m,n):         
            if m < 0 or m+1 > w or n < 0 or n+1 > h:
                return False
            if grid[m][n] == "0":
                return False
            if (m,n) in sdic:
                return False   
            sdic[(m,n)]=1            
            search(m+1,n)
            search(m-1,n) 
            search(m,n+1)   
            search(m,n-1)            
            return True
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if search(i,j):
                    count += 1
        return count

s = Solution()
print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))