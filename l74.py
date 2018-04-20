""" Search a 2D Matrix """

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def findrow():
            if not matrix:
                return False
            start = 0
            end = len(matrix) - 1

            while start + 1 < end:
                mid = start + (end-start)//2
                if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                    return mid
                elif matrix[mid][-1] < target:
                    start = mid
                else:
                    end = mid
            if matrix[start]:
                if matrix[start][0] <= target and matrix[start][-1] >= target:
                    return start
            if matrix[end]:
                if matrix[end][0] <= target and matrix[end][-1] >= target:
                    return end
            return False
        
        def findcol(row):
            if not row:
                return False
            start = 0
            end = len(row) - 1 
            while start + 1< end:
                mid =  start + (end-start)//2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    start = mid
                else:
                    end = mid
            if row[start] == target:
                return True
            if row[end] == target:
                return True
            return False
        
        rnum = findrow()
        if rnum is not False:
            return findcol(matrix[rnum])
        else:
            return False