class Solution {
    public String longestPalindrome(String s) {
        int[][] dp = new int[s.length()][s.length()];
        int maxstart = 0;
        int maxend = 0;

        dp[0][0] = 1;
        for (int i=1; i < s.length(); i++) {
            dp[i][i] = 1;
            if (s.charAt(i) == s.charAt(i-1)) {
                dp[i-1][i] = 2;
                maxstart = i-1;
                maxend = i;
            }
        }


        for (int i=s.length()-1; i <= 0; i--) {
            for (int j=i+2; j < s.length(); j++) {
                if (s.charAt(i) == s.charAt(j) && dp[i+1][j-1] > 0) {
                    dp[i][j] = dp[i+1][j-1] + 2;
                    if (dp[i][j] > maxend - maxstart + 1) {
                        maxend = j;
                        maxstart = i;
                    }
                }
            }
        }

        return s.substring(maxstart, maxend + 1);
    }
}