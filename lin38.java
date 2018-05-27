// Search a 2D Matrix II
// Write an efficient algorithm that searches for a value in an m x n matrix, return the occurrence of it.

public class Solution {
    /**
     * @param matrix: A list of lists of integers
     * @param target: An integer you want to search in matrix
     * @return: An integer indicate the total occurrence of target in the given matrix
     */
    public int searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0) {
            return 0;
        }
        if (matrix[0] == null || matrix[0].length ==0) {
            return 0;
        }

        int row = matrix.length -1, col = 0;
        int count = 0;

        while (row >= 0 && col < matrix[0].length) {
            if (matrix[row][col] < target) {
                col += 1;
            } else if (matrix[row][col] > target) {
                row -= 1;
            } else {
                count += 1;
                row -= 1;
                col += 1;
            }
        }
        return count;
    }
}