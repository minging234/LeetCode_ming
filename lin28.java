// Search a 2D Matrix

public class Solution {
    /**
     * @param matrix: matrix, a list of lists of integers
     * @param target: An integer
     * @return: a boolean, indicate whether matrix contains target
     */
    public boolean searchMatrix(int[][] matrix, int target) {
        // write your code here
        if (matrix == null || matrix.length == 0) {
            return false;
        }

        int start = 0;
        int end = matrix.length * matrix[0].length - 1;
        int row, col;

        while (start + 1 < end) {
            int mid = start + (end - start)/2;
            row = mid / matrix[0].length;
            col = mid % matrix[0].length;
            if (matrix[row][col] == target) {
                return true;
            } else if (matrix[row][col] < target) {
                start = mid;
            } else {
                end = mid;
            }
        }
        
        if (matrix[start / matrix[0].length][start % matrix[0].length] == target) {
            return true;
        } 
        if (matrix[end / matrix[0].length][end % matrix[0].length] == target) {
            return true;
        } 
        return false;     
    }
}