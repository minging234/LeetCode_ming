// Unique Paths II

class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
           if (obstacleGrid == null || obstacleGrid.length == 0 || obstacleGrid[0] == null || obstacleGrid[0].length == 0) {
               return 0;
           }
           
           int height = obstacleGrid.length;
           int wide = obstacleGrid[0].length;
           int[][] dp = new int[height][wide];

           if (obstacleGrid[0][0] == 1 || obstacleGrid[height - 1][wide - 1] == 1) {
               return 0;
           }

           dp[height - 1][wide - 1] = 1;

           for (int i = height - 1; i >= 0; i--) {
               for (int j = wide - 1; j >= 0; j--) {
                   if (obstacleGrid[i][j] == 1) {
                       continue;
                   }
                   if (i < height - 1) {
                       dp[i][j] += dp[i+1][j];
                   }
                   if (j < wide - 1) {
                       dp[i][j] += dp[i][j+1];
                   }
               }
           }

           return dp[0][0];
    }
}