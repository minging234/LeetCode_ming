// House Robber

class Solution {
    public int rob(int[] nums) {
        if (nums == null || nums.length == 0) {
            return -1;
        }
        int n = nums.length;

        int[][] dp = new int[n][n];

        for (int i = 0; i < n; i++) {
            dp[i][i] = nums[i];
        }

        for (int i = n-1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                int local = Integer.MIN_VALUE;
                if (i < n - 1) {
                    local = Math.max(dp[i+1][j], local);
                }
                if (i < n - 2) {
                    local = Math.max(dp[i+2][j] + nums[i], local);
                }
                if (j > 0) {
                    local = Math.max(dp[i][j-1], local);
                }
                if (j > 1) {
                    local = Math.max(dp[i][j-2] + nums[j], local);
                }
                dp[i][j] = local;
            }
        }
        return dp[0][n-1];
    }
}