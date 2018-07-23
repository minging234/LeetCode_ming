// Best Time to Buy and Sell Stock III

class Solution {
    public int maxProfit(int[] prices) {
        int[] first = new int[prices.length];
        int[] second = new int[prices.length];
        int ans = 0;

        int buy = Integer.MAX_VALUE;
        int sell = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < buy) {
                buy = prices[i];
                sell = 0;
            } else if (prices[i] > sell) {
                sell = prices[i];
            }
            first[i] = sell - buy;
        }

        buy = 0;
        sell = Integer.MIN_VALUE;

        for (int i = prices.length - 1; i >= 0; i--) {
            if (prices[i] > sell) {
                sell = prices[i];
            } else if (-prices[i] < buy) {
                buy = -prices[i];
                sell = 0;
            }
            second[i] = sell - buy;
        }

        ans = second[0];
        for (int i=1; i < prices.length; i++) {
            ans = Math.max(ans, first[i-1] + second[i]);
        }
        ans = Math.max(ans, first[prices.length-1]);
        return ans;
    }
}