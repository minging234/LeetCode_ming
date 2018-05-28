// Given a string s, find the longest palindromic subsequence's length in s. 

public class Solution {
    /**
     * @param s: the maximum length of s is 1000
     * @return: the longest palindromic subsequence's length
     */
    public int longestPalindromeSubseq(String s) {
        if (s == "" || s.length() == 0) return 0;
        int n = s.length();
        String rs = "";
        for (int i = n-1; i >= 0; i--) {
            rs += s.charAt(i);
        }
        int[][] dp = new int[n+1][n+1];

        for (int i = 1; i <= n; i ++) {
            for (int j = 1; j <=n ;j ++) {
                if (s.charAt(i-1) == rs.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        return dp[n][n];
    }
}