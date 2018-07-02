class Solution {
    public void rotate(int[][] matrix) {
        if (matrix == null || matrix[0] == null || matrix.length != matrix[0].length) {
            return;
        }

        int n = matrix.length;
        
        for (int i=0; i < n/2; i++) {
            for (int j=i; j < n - i -1; j++) {
                int x = i;
                int y = j;
                int temp = matrix[x][y];
                matrix[x][y] = matrix[n-1-y][x];
                matrix[n-1-y][x] = matrix[n-1-x][n-1-y];
                matrix[n-1-x][n-1-y] = matrix[y][n-1-x];
                matrix[y][n-1-x] = temp;
            }
        }
        return;
    }
}