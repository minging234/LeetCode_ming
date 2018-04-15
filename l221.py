class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        maxarea = 0
        if not matrix:
            return 0
        
        for i in range(len(matrix[0])):
            if matrix[0][i] == '1':
                maxarea = 1

        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = int(matrix[i-1][j]) + int(matrix[i][j])
            
            for m in range(len(matrix[0])):
                edge = matrix[i][m]
                left = right = -1
                n = m
                while matrix[i][m] <= matrix[i][n]:
                    left += 1
                    n -= 1
                    if n < 0:
                        break
                n = m 
                while matrix[i][m] <= matrix[i][n]:
                    right += 1
                    n += 1
                    if n == len(matrix[0]):
                        break
                if (left+right+1) >= edge:
                    maxarea = max(maxarea, edge*edge)

        return maxarea


s = Solution()
print(s.maximalSquare([["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]]))



"""
    my version is about how to find the max rectangle area in a matrix, and it should be more hard to do so
        maxarea = 0
        if not matrix:
            return 0
        
        def helper(heights):
            heights.append(0)
            stack = [-1]
            ans = 0
            for i in range(len(heights)):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    ans = max(ans, h * w)
                stack.append(i)
            heights.pop()
            return ans

        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = int(matrix[i-1][j]) + int(matrix[i][j])
            maxarea = max(maxarea, helper(matrix[i]))
        

        return maxarea



                print(left,right,(left+right),edge)



                for n in range(m+1, m + edge):
                    if n >= len(matrix[0]):
                        flag = False
                        break  
                    print(matrix[i][n],matrix[i][m])                      
                    if matrix[i][n] < matrix[i][m]:
                        edge = matrix[i][n]
                print(flag,edge,m, m + edge - 1)
                if flag:
                    maxarea = max(maxarea, edge*edge)

"""