import Math;

public class RMQ_ST {

    private int[][] dp;

    public RMQ_ST(int[] a) {
        int n = a.length;
        dp = new int[n+1][n+1];
        for (int i=1; i<=n; i++) dp[i][0]=a[i];
        for (int j=1; (1 << j) <= n; j++) {
            for(int i=1; i + (1 << j) -1 <= n; i++) {
                dp[i][j] = Math.max(dp[i][j-1], dp[i + (1<<(j - 1))][j-1]);
            }
        }
    }

    public int RMQ(int r, int l) {
        int k = 0; 
        while((1 << (k+1)) <= r - l + 1) {
            k ++;
        }
        return Math.max(dp[l][k], dp[r - (1 << k) + 1][k]);
    }

}