""" Rotate Image """

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for t in range(n//2):
            for i in range(t,n-t-1):
                x = i
                y = t

                a = matrix[y][n-1-x]
                matrix[y][n-1-x] = matrix[x][y]

                b = matrix[n-1-x][n-1-y]
                matrix[n-1-x][n-1-y] = a

                c = matrix[n-1-y][x]
                matrix[n-1-y][x] = b

                matrix[x][y] = c
        print(matrix)
        return


S = Solution()
S.rotate([[1,2,3],[4,5,6],[7,8,9]])