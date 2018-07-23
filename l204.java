// Count Primes

class Solution {
    public int countPrimes(int n) {
        int[] dp = new int[n];
        int ans = 0;

        for (int i=2; i < n; i++) {
            if (dp[i] == 0) {
                ans += 1;
                if (i*i < n) {
                    for (int j = 2; j*i < n; j++) {
                        dp[j*i] = 1; 
                    }
                }
            }
        }
        return ans;
    }
}