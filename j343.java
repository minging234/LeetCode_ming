class Solution {
    public int integerBreak(int n) {
        int[] dp = new int[n];
        dp[1] = 1;
        dp[2] = 1;
        for (int i = 3; i < n+1; i++ ){
            for (int j = 1; j < i/2; j++ ){
                dp[i] = Math.max(dp[i], dp[j]* dp[i-j]);
            }
        }
        return dp[n];

    }
}